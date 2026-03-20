import pytest
from pages.basic_auth_page import BasicAuthPage
from utils.logger import Logger


class TestBasicAuth:

    def test_basic_auth_success(self, browser):
        page = BasicAuthPage(browser)
        page.open_with_auth("admin", "admin")
        page.wait_for_page_to_load()

        message = page.get_success_message()
        Logger.info(f"Получено сообщение: {message}")

        assert "Congratulations" in message, \
            f"Ожидалось сообщение с 'Congratulations', получено: {message}"
