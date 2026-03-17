import pytest
from browser import Browser


@pytest.fixture(scope="session", autouse=True)
def browser_quit():
    yield
    Browser.quit()
