import os

import requests

BASE_URL = "https://api.trello.com/1/"

HEADERS = {"Accept": "application/json"}

BASE_QUERY = {"key": os.getenv("TRELLO_API_KEY"), "token": os.getenv("TRELLO_TOKEN")}

BOARD_ID = os.environ["TRELLO_BOARD_ID"]


list_names_to_id = {
    list_["name"]: list_["id"]
    for list_ in requests.get(
        BASE_URL + f"boards/{BOARD_ID}/lists", headers=HEADERS, params=BASE_QUERY
    ).json()
}
list_ids_to_name = {v: k for k, v in list_names_to_id.items()}


def get_items():
    response = requests.get(
        BASE_URL + f"boards/{BOARD_ID}/cards",
        headers=HEADERS,
        params=BASE_QUERY,
    )

    return [
        {
            "id": card["id"],
            "status": list_ids_to_name[card["idList"]],
            "title": card["name"],
        }
        for card in response.json()
    ]


def add_item(title):
    query = {"idList": list_names_to_id["To do"], "name": title}
    requests.post(BASE_URL + "/cards", headers=HEADERS, params=BASE_QUERY | query)


def mark_item_done(id):
    query = {"idList": list_names_to_id["Done"]}
    res = requests.put(BASE_URL + f"cards/{id}", headers=HEADERS, params=BASE_QUERY | query)
