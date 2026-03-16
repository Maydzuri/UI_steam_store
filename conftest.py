import pytest
from browser import Browser


_browser = Browser()

@pytest.fixture(scope="function")
def driver(request):
    language = request.node.callspec.params.get('language', 'en')
    driver = _browser.get_driver(language)
    yield driver
    _browser.quit()
