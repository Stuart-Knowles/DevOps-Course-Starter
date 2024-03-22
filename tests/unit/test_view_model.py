import pytest

from todo_app.src.trello import Item
from todo_app.src.view import ViewModel


MOCK_ITEMS = [
    Item(id="id_1", name="1", status="To do"),
    Item(id="id_2", name="2", status="Done"),
]


@pytest.fixture(name="default_mock_view")
def get_default_mock_view():
    return ViewModel(items=MOCK_ITEMS)


def test_get_items(default_mock_view):
    assert default_mock_view.items == MOCK_ITEMS


def test_get_to_do_items(default_mock_view):
    assert default_mock_view.to_do_items == [MOCK_ITEMS[0]]


def test_get_done_items(default_mock_view):
    assert default_mock_view.done_items == [MOCK_ITEMS[1]]
