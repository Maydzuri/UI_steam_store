import pytest
from browser import Browser, Language


@pytest.fixture
def browser(request):
    language = request.node.callspec.params.get('language', Language.ENGLISH)
    driver = Browser(language)
    yield driver
    Browser.quit()
