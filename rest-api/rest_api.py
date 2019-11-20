from typing import Any, Dict, List, Optional, Union


class RestAPI:
    def __init__(
        self,
        database: Optional[
            Dict[
                str,
                Union[
                    List[Dict[str, Union[str, float]]],
                    List[Dict[str, Union[str, Dict[str, float], float]]],
                    List[
                        Union[
                            Dict[str, Union[str, float]],
                            Dict[str, Union[str, Dict[str, float], float]],
                        ]
                    ],
                    List[Any],
                ],
            ]
        ] = None,
    ) -> None:
        pass

    def get(self, url: str, payload: Optional[str] = None) -> None:
        pass

    def post(self, url: str, payload: Optional[str] = None) -> None:
        pass
