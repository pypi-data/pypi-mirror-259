from datetime import datetime
from typing import List

import pandas as pd
from pydantic import BaseModel, Field
from tabulate import tabulate

from chaiverse.schemas.leaderboard_row_schema import LeaderboardRow
from chaiverse.lib.date_tools import utc_string

DEFAULT_LEADERBOARD_HEADER_MAPPING = {
    'double_thumbs_up_rate': '👍👍_rate',
    'thumbs_up_rate': '👍👍+👍_rate',
    'single_thumbs_up_rate': '👍_rate',
    'thumbs_down_rate': '👎_rate',
}

DEFAULT_LEADERBOARD_COLUMNS = [
    'model_name', 
    'elo_rating',
    'win_rate',
    'num_battles',
    'double_thumbs_up_rate',
    'thumbs_down_rate',
    'feedback_count',
    'model_score',
    'safety_score',
    'status',
    'developer_uid',
    'submission_id',
    'language_model',
    'reward_model',
    'timestamp'
]


class Leaderboard(BaseModel):
    timestamp: datetime = Field(default_factory=utc_string)
    leaderboard_rows: List[LeaderboardRow]

    def to_dataframe(self):
        leaderboard_rows = [row.all_fields_dict() for row in self.leaderboard_rows]
        df = pd.DataFrame.from_records(leaderboard_rows)
        df.reset_index(drop=True)
        return df

    def to_display_dataframe(self, columns=None, header_mapping=None):
        df = self.to_dataframe()
        columns = columns or DEFAULT_LEADERBOARD_COLUMNS
        df = df[[column for column in columns if column in df.columns]]
        header_mapping = header_mapping or DEFAULT_LEADERBOARD_HEADER_MAPPING
        df.reset_index(drop=True)
        df = df.rename(columns=header_mapping)
        return df
    
    def to_tabulate(self, *args, **kwargs):
        df = self.to_dataframe(*args, **kwargs)
        tabulated = tabulate(df.round(3), headers=df.columns, numalign='decimal')
        return tabulated
