import pytest
from browser import Browser


@pytest.fixture(scope="function")
def driver(request):
    language = request.node.callspec.params.get('language', 'en')
    browser = Browser()
    driver = browser.get_driver(language)
    driver.delete_all_cookies()
    yield driver
    browser.quit()
