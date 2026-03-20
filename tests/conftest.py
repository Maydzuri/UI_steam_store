import pytest
from browser.browser import Browser


@pytest.fixture
def browser():
    b = Browser()
    yield b
    b.quit()
