import requests
from typing import Any


class AiAssist:
    def __init__(self) -> None:
        self.agent_url = "http://osyris-1a1e5.uc.r.appspot.com/tabular_ds_agent"

    def get_code_str(self, payload) -> Any:
        res = requests.post(self.agent_url, json=payload)
        if res.status_code == 200:
            return res.json()['code']
        else:
            print(
                f"Failed to retrieve data, status code: {res.status_code}")
            return None
