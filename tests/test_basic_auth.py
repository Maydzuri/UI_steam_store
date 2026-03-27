from pages.basic_auth_page import BasicAuthPage
from utils.logger import Logger


class TestBasicAuth:

    def test_basic_auth_success(self, browser):
        url = "http://admin:admin@the-internet.herokuapp.com/basic_auth"
        browser.get(url)

        page = BasicAuthPage(browser)
        page.wait_for_open()

        message = page.get_success_message()
        Logger.info(f"Получено сообщение: {message}")

        expected_text = "Congratulations"
        assert expected_text in message, \
            f"Ожидалось сообщение, содержащее '{expected_text}', но получено: '{message}'"
