import pytest
from browser.browser import Browser
from pages.alerts_page import AlertsPage
from pages.context_menu_page import ContextMenuPage


@pytest.fixture
def browser():
    b = Browser()
    yield b
    b.quit()


@pytest.fixture
def alerts_page(browser):
    browser.get("https://the-internet.herokuapp.com/javascript_alerts")
    page = AlertsPage(browser)
    page.wait_for_open()
    return page


@pytest.fixture
def context_menu_page(browser):
    browser.get("https://the-internet.herokuapp.com/context_menu")
    page = ContextMenuPage(browser)
    page.wait_for_open()
    return page
