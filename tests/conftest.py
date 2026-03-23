import pytest
from browser.browser import Browser
from pages.alerts_page import AlertsPage
from pages.context_menu_page import ContextMenuPage
from pages.horizontal_slider_page import HorizontalSliderPage


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

@pytest.fixture
def slider_page(browser):
    browser.get("https://the-internet.herokuapp.com/horizontal_slider")
    page = HorizontalSliderPage(browser)
    page.wait_for_open()
    return page
