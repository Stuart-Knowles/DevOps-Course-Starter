import os

import pytest
import requests_mock

from todo_app.src.trello.config import get_trello_config

from .mock_trello_data import MOCK_LISTS, MOCK_ITEMS


@pytest.fixture
def mock_trello_api():
    base_url = f"https://api.trello.com/1/boards/{os.environ['TRELLO_BOARD_ID']}"
    with requests_mock.Mocker() as m:
        m.get(f"{base_url}/lists", json=MOCK_LISTS)
        m.get(f"{base_url}/cards", json=MOCK_ITEMS)
        yield m


def test_index_page(test_client, mock_trello_api):
    response = test_client.get("/")
    html = response.data.decode()

    assert response.status_code == 200
    assert mock_trello_api.call_count == 2
    assert all([item["name"] in html for item in MOCK_ITEMS])
