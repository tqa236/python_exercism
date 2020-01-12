import json
from typing import Any, Dict, List, Optional, Union


class RestAPI:
    def __init__(
        self,
        database: Dict[
            str,
            Union[
                List[Dict[str, Union[str, Dict[str, float], float]]],
                List[Dict[str, Union[str, float]]],
                List[
                    Union[
                        Dict[str, Union[str, float]],
                        Dict[str, Union[str, Dict[str, float], float]],
                    ]
                ],
                List[Any],
            ],
        ],
    ) -> None:
        self.database = database

    def get(self, url: str, payload: Optional[str] = None) -> None:
        return json.dumps(self.database)

    def post(self, url: str, payload: Optional[str] = None) -> None:
        pass
