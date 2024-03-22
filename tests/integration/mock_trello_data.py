from todo_app.src.trello import Item

MOCK_LISTS = [
    {
        "id": "test-list-id-1",
        "name": "To do",
        "closed": False,
        "color": None,
        "idBoard": "test-trello-board-id",
        "pos": 1,
        "subscribed": False,
        "softLimit": None,
    },
    {
        "id": "test-list-id-2",
        "name": "Done",
        "closed": False,
        "color": None,
        "idBoard": "test-trello-board-id",
        "pos": 3,
        "subscribed": False,
        "softLimit": None,
    },
]

MOCK_ITEMS = [
    {
        "id": "test-card-id-1",
        "idBoard": "test-trello-board-id",
        "idList": "test-list-id-1",
        "name": "Test Card 1",
        "pos": 1,
    },
    {
        "id": "test-card-id-2",
        "idBoard": "test-trello-board-id",
        "idList": "test-list-id-2",
        "name": "Test Card 2",
        "pos": 32770,
    },
]
