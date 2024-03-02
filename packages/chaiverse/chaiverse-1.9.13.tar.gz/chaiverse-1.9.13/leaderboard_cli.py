from chaiverse.http_client import SubmitterClient
from chaiverse.schemas import Leaderboard
from chaiverse import config


def get_leaderboard(developer_key):
    submitter_client = SubmitterClient(developer_key=developer_key)
    leaderboard = submitter_client.get(config.LATEST_LEADERBOARD_ENDPOINT)
    leaderboard = Leaderboard(**leaderboard)
    return leaderboard


def display_leaderboard(developer_key):
    leaderboard = get_leaderboard(developer_key)
    print(leaderboard.to_tabulate())
