import os
from functools import cache
import requests


class _TrelloConfig:
    def __init__(self):
        self.base_url = "https://api.trello.com/1/"
        self.headers = {"Accept": "application/json"}
        self.base_query = {"key": os.environ["TRELLO_API_KEY"], "token": os.environ["TRELLO_TOKEN"]}
        self.board_id = os.environ["TRELLO_BOARD_ID"]
        self._list_names_to_id = {
            list_["name"]: list_["id"]
            for list_ in requests.get(
                self.base_url + f"boards/{self.board_id}/lists",
                headers=self.headers,
                params=self.base_query,
            ).json()
        }
        self._list_ids_to_name = {v: k for k, v in self._list_names_to_id.items()}

    def get_list_id_from_name(self, name: str) -> str:
        return self._list_names_to_id[name]

    def get_list_name_from_id(self, id: str) -> str:
        return self._list_ids_to_name[id]


@cache
def get_trello_config():
    return _TrelloConfig()
