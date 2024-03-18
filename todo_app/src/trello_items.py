import os
from dataclasses import dataclass

import requests

from .trello_config import get_trello_config


@dataclass
class Item:
    id: str
    name: str
    status: str

    @classmethod
    def from_trello(cls, card):
        config = get_trello_config()
        return cls(
            id=card["id"], name=card["name"], status=config.get_list_name_from_id(card["idList"])
        )


def get_items():
    config = get_trello_config()
    response = requests.get(
        config.base_url + f"boards/{config.board_id}/cards",
        headers=config.headers,
        params=config.base_query,
    )

    return [Item.from_trello(card) for card in response.json()]


def add_item(title):
    config = get_trello_config()
    query = {"idList": config.get_list_id_from_name("To do"), "name": title}
    requests.post(
        config.base_url + "/cards", headers=config.headers, params=config.base_query | query
    )


def mark_item_done(id):
    config = get_trello_config()
    query = {"idList": config.get_list_id_from_name("Done")}
    res = requests.put(
        config.base_url + f"cards/{id}", headers=config.headers, params=config.base_query | query
    )
