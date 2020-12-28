from typing import List
import datetime
import pytz
from connections import get_connection
import database

class Option:
    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id
        self.text = option_text
        self.poll_id = poll_id

    def __repr__(self) -> str:
        return f"Option({self.text!r}, {self.poll_id!r}, {self.id!r})"

    def save(self):
        with get_connection() as connection:
            new_option_id = database.add_option(connection, self.text, self.poll_id)
            self.id = new_option_id

    @classmethod
    def get(cls, option_id: int) -> "Option":
        with get_connection() as connection:
            option = database.get_option(connection, option_id)
            return cls(option[1], option[2], option[0])

    def vote(self, username: str):
        with get_connection() as connection:
            current_datetime_utc = datetime.datetime.now(tz=pytz.utc)
            current_timestamp = current_datetime_utc.timestamp()
            database.add_poll_vote(connection, username, current_timestamp, self.id)

    @property
    def votes(self) -> List[database.Vote]:
        with get_connection() as connection:
            votes = database.get_votes_for_option(connection, self.id)
            return votes
