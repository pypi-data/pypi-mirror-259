import itertools
import sys
import time
from typing import List, Optional

from pydantic import BaseModel, Extra, PrivateAttr, validator, Field


from chaiverse import errors, utils
from chaiverse.cli_utils.login_cli import auto_authenticate
from chaiverse.http_client import SubmitterClient
from chaiverse import config, formatters

if 'ipykernel' in sys.modules:
    from IPython.core.display import display


class GenerationParams(BaseModel, extra=Extra.allow):
    temperature: float = Field(..., description="Controls the randomness in the model's output. A higher temperature increases randomness.")
    top_p: float = Field(..., description="The model considers only the most probable tokens with probability above this threshold.")
    top_k: int = Field(..., description="Number of highest probability tokens considered at each step of the generation process.")
    presence_penalty: Optional[float] = Field(None, description="Encourages the model to use new and unique words by penalizing words that have already appeared in the text.")
    frequency_penalty: Optional[float] = Field(None, description="Encourages the model to use new and unique words by penalizing tokens based on their frequency in the text so far.")
    stopping_words: Optional[List[str]] = Field(["\n"], description="Words or tokens that signal the model to stop generating further text.")
    max_input_tokens: Optional[int] = Field(config.DEFAULT_MAX_INPUT_TOKENS, description="The maximum number of tokens the model can consider from the input prompt.")
    best_of: Optional[int] = Field(config.DEFAULT_BEST_OF, description="Number of outputs the process produce, and select the best one among them under defined criteria.")

    _validation_errors: List[str] = PrivateAttr(default=[])

    def validate_currently_supported_format(self):
        # Validation is NOT done using pydantic validator for backward
        # compatibility
        self._validate_parameters()
        self._validate_presence_penalty()
        self._validate_frequency_penalty()
        self._validate_temperature()
        self._validate_top_k()
        self._validate_top_p()
        self._validate_max_input_tokens()
        self._validate_best_of()

        if self._validation_errors:
            error_messages = ', '.join(self._validation_errors)
            message = f"Generation Parameters validation failed with the following errors: {error_messages}"
            raise errors.ValidationError(message)

    def _validate_parameters(self):
        required_params = {'temperature', 'top_p', 'top_k', 'presence_penalty', 'frequency_penalty'}
        recognised_params = required_params.union({'max_input_tokens', 'stopping_words', 'best_of'})
        actual_params = set(self.dict(exclude_none=True).keys())

        # check there are no extra parameters
        extra_params = sorted(actual_params - recognised_params)
        if len(extra_params) > 0:
            msg = f'unrecognised generation parameters: {", ".join(extra_params)}'
            self._validation_errors.append(msg)

        # check there are no missing parameters
        missing_params = sorted(required_params - actual_params)
        if len(missing_params) > 0:
            msg = f'missing generation parameters: {", ".join(missing_params)}'
            self._validation_errors.append(msg)

    def _validate_presence_penalty(self):
        if self.presence_penalty is not None and not -2 <= self.presence_penalty <= 2:
            msg = f"`presence_penalty` must be in [-2, 2], got {self.presence_penalty}"
            self._validation_errors.append(msg)

    def _validate_frequency_penalty(self):
        if self.frequency_penalty is not None and not -2 <= self.frequency_penalty <= 2:
            msg = f"`frequency_penalty` must be in [-2, 2], got {self.frequency_penalty}"
            self._validation_errors.append(msg)

    def _validate_temperature(self):
        if self.temperature is not None and self.temperature < 0:
            self._validation_errors.append("`temperature` must be positive")

    def _validate_top_k(self):
        if self.top_k is not None and self.top_k <= 0:
            self._validation_errors.append("`top_k` must be greater than 0")

    def _validate_top_p(self):
        if self.top_p is not None and (self.top_p <= 0 or self.top_p > 1.0):
            self._validation_errors.append("`top_p` must be in (0, 1]")

    def _validate_best_of(self):
        if self.best_of is not None and (self.best_of <= 0 or self.best_of > 16):
            self._validation_errors.append("`best_of` must be in [1, 16]")

    def _validate_max_input_tokens(self):
        min_tokens = config.DEFAULT_MAX_INPUT_TOKENS
        max_tokens = 4096
        is_not_none = self.max_input_tokens is not None
        is_not_in_correct_range = not (min_tokens <= self.max_input_tokens <= max_tokens)
        if is_not_none and is_not_in_correct_range:
            msg = f"`max_input_tokens` must be in [{min_tokens}, {max_tokens}], got {self.max_input_tokens}"
            self._validation_errors.append(msg)


class FrontEndSubmissionRequest(BaseModel):
    model_repo: str = Field(..., description="Huggingface model repo url.")
    reward_repo: Optional[str] = Field(None, description="Huggingface reward model repo url.")
    generation_params: GenerationParams
    formatter: formatters.PromptFormatter = Field(formatters.PygmalionFormatter, description="Prompt formatter for model.")
    reward_formatter: formatters.PromptFormatter = Field(formatters.PygmalionFormatter, description="Prompt formatter for reward model.")
    model_name: Optional[str] = Field(None, description="name of your model.")
    hf_auth_token: Optional[str] = Field(None, description="Your huggingface authentication toekn.")

    @validator("generation_params")
    def check_generation_params(cls, generation_params):
        generation_params.validate_currently_supported_format()
        return generation_params


class FrontEndBlendSubmissionRequest(BaseModel):
    submissions: List[str] = Field(..., description="submission_id for models to include in the blend.")
    model_name: Optional[str] = Field(None, description="name of your model.")


class ModelSubmitter:
    """
    Submits a model to the Guanaco service and exposes it to beta-testers on the Chai app.

    Attributes
    --------------
    developer_key : str
    verbose       : str - Print deployment logs

    Methods
    --------------
    submit(submission_params)
    Submits the model to the Guanaco service.

    Example usage:
    --------------
    submitter = ModelSubmitter(developer_key)
    submitter.submit(submission_params)
    """

    @auto_authenticate
    def __init__(self, developer_key=None, verbose=False):
        self.developer_key = developer_key
        self.verbose = verbose
        self._animation = self._spinner_animation_generator()
        self._progress = 0
        self._sleep_time = 0.5
        self._get_request_interval = int(10 / self._sleep_time)
        self._logs_cache = []

    def submit(self, submission_params):
        """
        Submits the model to the Guanaco service and wait for the deployment to finish.

        submission_params: dict
            model_repo: str - HuggingFace repo
            hf_auth_token (optional): str - A read-only token used to access model_repo
            generation_params: dict
                temperature: float
                top_p: float
                top_k: int
                repetition_penalty: float
            formatter (optional): PromptFormatter
            reward_formatter (optional): PromptFormatter
            model_name (optional): str - custom alias for your model
        """
        submission_params = submission_params.copy()
        submission_params = self._preprocess_submission(submission_params)
        return self._handle_submit(submit_model, submission_params)

    def _preprocess_submission(self, submission_params):
        if submission_params.get('formatter'):
            submission_params["formatter"] = submission_params["formatter"].dict()
        if submission_params.get("reward_formatter"):
            submission_params["reward_formatter"] = submission_params["reward_formatter"].dict()
        return submission_params

    def submit_blend(self, submission_params):
        """
        Submits blend to the Guanaco service and wait for the deployment to finish.

        submission_params: dict
            submissions: list - submission_ids for the models in the blend
            model_name (optional): str - custom alias for your model
        """
        return self._handle_submit(submit_model_blend, submission_params)

    def _handle_submit(self, submission_func, submission_params):
        check_user_accepts_eula(self.developer_key)
        submission_response = submission_func(submission_params, self.developer_key)
        submission_id = submission_response.get('submission_id')
        self._print_submission_header(submission_id)
        status = self._wait_for_model_submission(submission_id)
        self._print_submission_result(status)
        self._progress = 0
        return submission_id

    def _wait_for_model_submission(self, submission_id):
        status = 'pending'
        while status not in {'deployed', 'failed', 'inactive'}:
            status = self._get_submission_status(submission_id)
            self._display_animation(status)
            time.sleep(self._sleep_time)
        return status

    def _get_submission_status(self, submission_id):
        self._progress += 1
        status = 'pending'
        if self._progress % self._get_request_interval == 0:
            model_info = get_model_info(submission_id, self.developer_key)
            self._print_latest_logs(model_info)
            status = model_info.get('status')
        return status

    def _spinner_animation_generator(self):
        animations = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
        return itertools.cycle(animations)

    def _display_animation(self, status):
        text = f" {next(self._animation)} {status}..."
        if 'ipykernel' in sys.modules:
            display(text, display_id="animation")
        else:
            print(text, end='\r')

    def _print_submission_header(self, submission_id):
        utils.print_color(f'\nModel Submission ID: {submission_id}', 'green')
        print("Your model is being deployed to Chaiverse, please wait for approximately 10 minutes...")

    def _print_submission_result(self, status):
        success = status == 'deployed'
        text_success = 'Model successfully deployed!'
        text_failed = 'Model deployment failed, please seek help on our Discord channel'
        text = text_success if success else text_failed
        color = 'green' if success else 'red'
        print('\n')
        utils.print_color(f'\n{text}', color)

    def _print_latest_logs(self, model_info):
        if self.verbose:
            logs = model_info.get("logs", [])
            num_new_logs = len(logs) - len(self._logs_cache)
            new_logs = logs[-num_new_logs:] if num_new_logs else []
            self._logs_cache += new_logs
            for log in new_logs:
                message = utils.parse_log_entry(log)
                print(message)


@auto_authenticate
def submit_model(model_submission: dict, developer_key=None):
    http_client = SubmitterClient(developer_key)
    response = http_client.post(endpoint=config.SUBMISSION_ENDPOINT, data=model_submission)
    return response


@auto_authenticate
def submit_model_blend(model_submission: dict, developer_key=None):
    http_client = SubmitterClient(developer_key)
    response = http_client.post(endpoint=config.BLEND_SUBMISSION_ENDPOINT, data=model_submission)
    return response


@auto_authenticate
def get_model_info(submission_id, developer_key=None):
    http_client = SubmitterClient(developer_key)
    response = http_client.get(endpoint=config.INFO_ENDPOINT, submission_id=submission_id)
    return response


@auto_authenticate
def evaluate_model(submission_id, developer_key=None):
    http_client = SubmitterClient(developer_key)
    response = http_client.get(endpoint=config.EVALUATE_ENDPOINT, submission_id=submission_id)
    return response


@auto_authenticate
def get_my_submissions(developer_key=None):
    http_client = SubmitterClient(developer_key)
    response = http_client.get(endpoint=config.ALL_SUBMISSION_STATUS_ENDPOINT)
    return response


@auto_authenticate
def deactivate_model(submission_id, developer_key=None):
    http_client = SubmitterClient(developer_key)
    response = http_client.get(endpoint=config.DEACTIVATE_ENDPOINT,submission_id=submission_id)
    print(response)
    return response


@auto_authenticate
def redeploy_model(submission_id, developer_key=None):
    http_client = SubmitterClient(developer_key)
    response = http_client.get(endpoint=config.REDEPLOY_ENDPOINT, submission_id=submission_id)
    print(response)
    return response


@auto_authenticate
def teardown_model(submission_id, developer_key=None):
    http_client = SubmitterClient(developer_key)
    response = http_client.get(endpoint=config.TEARDOWN_ENDPOINT, submission_id=submission_id)
    print(response)
    return response


@auto_authenticate
def check_user_accepts_eula(developer_key):
    text = "Thank you! Before submitting a model, please acknowledge that you have"\
           " read our End-user license agreement (EULA),"\
           "\nwhich can be found at: www.chai-research.com/competition-eula.html 🥳."\
           "\nPlease type 'accept' to confirm that you have read and agree with our EULA: "
    input_text = input(text)
    if input_text.lower().strip() != 'accept':
        raise ValueError('In order to submit a model, you must agree with our EULA 😢')

