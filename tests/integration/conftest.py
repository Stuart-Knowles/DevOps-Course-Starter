import pytest
from dotenv import load_dotenv

from todo_app.app import create_app


@pytest.fixture(autouse=True, scope="package")
def environment():
    load_dotenv(".env.test")


@pytest.fixture(scope="package")
def test_client(environment):
    app = create_app()
    with app.test_client() as client:
        yield client
