import json
from typing import Optional


class RestAPI:
    def __init__(self, database):
        self.database = database

    def get(self, url: str, payload: Optional[str] = None) -> None:
        return json.dumps(self.database)

    def post(self, url: str, payload: Optional[str] = None) -> None:
        pass
