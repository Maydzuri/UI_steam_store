import pytest
from browser.browser import Browser
from pages.alerts_page import AlertsPage
from pages.context_menu_page import ContextMenuPage
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.hovers_page import HoversPage
from pages.windows_page import WindowsPage
from pages.frames_page import FramesPage
from pages.dynamic_content_page import DynamicContentPage
from pages.infinite_scroll_page import InfiniteScrollPage
from pages.upload_page import UploadPage
from pages.upload_dialog_page import UploadDialogPage
from pages.upload_drag_drop_page import UploadDragDropPage



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

@pytest.fixture
def hovers_page(browser):
    browser.get("https://the-internet.herokuapp.com/hovers")
    page = HoversPage(browser)
    page.wait_for_open()
    return page

@pytest.fixture
def windows_page(browser):
    browser.get("https://the-internet.herokuapp.com/windows")
    page = WindowsPage(browser)
    page.wait_for_open()
    return page

@pytest.fixture
def frames_page(browser):
    browser.get("https://demoqa.com/frames")
    page = FramesPage(browser)
    page.wait_for_open()
    return page

@pytest.fixture
def dynamic_content_page(browser):
    browser.get("https://the-internet.herokuapp.com/dynamic_content")
    page = DynamicContentPage(browser)
    page.wait_for_open()
    return page

@pytest.fixture
def infinite_scroll_page(browser):
    browser.get("https://the-internet.herokuapp.com/infinite_scroll")
    page = InfiniteScrollPage(browser)
    page.wait_for_open()
    return page

@pytest.fixture
def upload_page(browser):
    browser.get("https://the-internet.herokuapp.com/upload")
    page = UploadPage(browser)
    page.wait_for_open()
    return page

@pytest.fixture
def upload_dialog_page(browser):
    browser.get("https://the-internet.herokuapp.com/upload")
    page = UploadDialogPage(browser)
    page.wait_for_open()
    return page

@pytest.fixture
def upload_drag_drop_page(browser):
    browser.get("https://the-internet.herokuapp.com/upload")
    page = UploadDragDropPage(browser)
    page.wait_for_open()
    return page
