from datetime import datetime
from typing import List, Union

from pydantic import BaseModel

from chaiverse.schemas.leaderboard_row_schema import LeaderboardRow


class Leaderboard(BaseModel):
    timestamp: datetime
    leaderboard_rows: List[LeaderboardRow]