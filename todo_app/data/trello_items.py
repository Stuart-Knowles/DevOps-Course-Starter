import json
import os

import requests

BASE_URL = "https://api.trello.com/1/"

HEADERS = {"Accept": "application/json"}

BASE_QUERY = {"key": os.getenv("TRELLO_API_KEY"), "token": os.getenv("TRELLO_TOKEN")}

LIST_ID = os.getenv("TRELLO_LIST_ID")


def get_items():
    response = requests.get(
        BASE_URL + f"lists/{LIST_ID}/cards",
        headers=HEADERS,
        params=BASE_QUERY,
    )

    return [
        {
            "id": card["idShort"],
            "status": "Complete" if card["closed"] else "Not Started",
            "title": card["name"],
        }
        for card in json.loads(response.text)
    ]


def add_item(title):
    query = {"idList": LIST_ID, "name": title}
    requests.post(BASE_URL + "/cards", headers=HEADERS, params=BASE_QUERY | query)
