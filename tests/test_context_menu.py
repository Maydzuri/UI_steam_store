import pytest
from pages.context_menu_page import ContextMenuPage
from utils.logger import Logger


class TestContextMenu:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        browser.get("https://the-internet.herokuapp.com/context_menu")
        self.page = ContextMenuPage(browser)
        self.page.wait_for_open()

    def test_context_menu(self, browser):
        self.page.right_click()

        alert_text = browser.accept_alert()
        Logger.info(f"Текст алерта: {alert_text}")

        assert alert_text == "You selected a context menu", \
            f"Ожидался текст 'You selected a context menu', получен '{alert_text}'"
