from datetime import datetime
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Extra, Field
import pytz


def us_pacific_timestamp():
    return datetime.now(pytz.timezone('US/Pacific'))


class BaseLeaderboardRow(BaseModel, extra=Extra.allow):
    developer_uid: str
    submission_id: str
    model_name: Optional[str]
    status: str
    timestamp: datetime = Field(default_factory=us_pacific_timestamp)

    double_thumbs_up: int = 0
    thumbs_up: int = 0
    thumbs_down: int = 0

    elo_rating: float = 1000
    num_battles: int = 0
    num_wins: int = 0
    
    @property
    def model_display_name(self):
        name = self.model_name if self.model_name else self.submission_id
        return name

    @property
    def base_model(self):
        raise NotImplementedError('base_model')

    @property
    def reward_model(self):
        raise NotImplementedError('reward_model')
    
    @property
    def model_size(self):
        raise NotImplementedError('model_size')


class BasicLeaderboardRow(BaseLeaderboardRow):
    submission_type: Literal['basic'] = Field(default_factory=lambda: 'basic')
    model_repo: str
    reward_repo: str
    model_num_parameters: float

    @property
    def base_model(self):
        return self.model_repo

    @property
    def reward_model(self):
        return self.reward_repo
    
    @property
    def model_size(self):
        size_gb = round(self.model_num_parameters / 1e9)
        size_gb = f'{size_gb}B'
        return size_gb


class BlendLeaderboardRow(BaseLeaderboardRow):
    submission_type: Literal['blend'] = Field(default='blend')
    submissions: List[str]

    @property
    def submission_type(self):
        return 'blend'

    @property
    def base_model(self):
        return ','.join(self.submissions)
    
    @property
    def reward_model(self):
        return 'random'
    
    @property
    def model_size(self):
        return 'n/a'


class RewardBlendLeaderboardRow(BaseLeaderboardRow):
    submission_type: Literal['reward_blend'] = Field(default='reward_blend')
    reward_repo: str

    submissions: List[str]
    num_samples: int    

    @property
    def base_model(self):
        pseudo_base_model = ','.join(self.submissions)
        return pseudo_base_model    

    @property
    def reward_model(self):
        return self.reward_repo
    
    @property
    def model_size(self):
        return 'n/a'


class TaggedSubmissionID(BaseModel):
    submission_id: str
    tags: Optional[List[str]] = None


class RoutedBlendLeaderboardRow(BaseLeaderboardRow):
    submission_type: Literal['routed_blend'] = Field(default='routed_blend')
    router: str
    tagged_submissions: List[TaggedSubmissionID]

    @property
    def base_model(self):
        tagged_submissions = []
        for tagged_submission in self.tagged_submissions:
            tags = '|'.join(tagged_submission.tags)
            tagged_submissions.append(f'{tagged_submission.submission_id}:{tags}')
        pseudo_base_model = ','.join(tagged_submissions)
        return pseudo_base_model
    
    @property
    def reward_model(self):
        return self.router

    @property
    def model_size(self):
        return 'n/a'


LeaderboardRow = Union[
    BlendLeaderboardRow,
    RewardBlendLeaderboardRow,
    RoutedBlendLeaderboardRow,
    BasicLeaderboardRow,
]
