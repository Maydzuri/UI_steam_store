from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser.browser import Browser
from pages.base_page import BasePage
from utils.logger import Logger



class BasicAuthPage(BasePage):

    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'example')]/p")

    def __init__(self, browser: Browser):
        super().__init__(browser, name="BasicAuthPage")
        self._message_locator = self.SUCCESS_MESSAGE

    def open_with_auth(self, username: str, password: str):
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        Logger.info(f"Открытие страницы с пользователем {username}")
        self.browser.get(url)

    def wait_for_page_to_load(self, timeout: int = None):
        timeout = timeout or self.browser.default_timeout
        Logger.info("Ожидание загрузки страницы Basic Auth")

        self.browser.wait_for_url_contains("basic_auth", timeout)

        WebDriverWait(self.browser.driver, timeout).until(
            EC.visibility_of_element_located(self._message_locator)
        )

        text = self._get_message_text(timeout)
        assert text != "", "Сообщение об успехе пустое"

    def get_success_message(self, timeout: int = None) -> str:
        return self._get_message_text(timeout)

    def _get_message_text(self, timeout: int = None) -> str:
        timeout = timeout or self.browser.default_timeout

        element = WebDriverWait(self.browser.driver, timeout).until(
            EC.visibility_of_element_located(self._message_locator)
        )

        text = element.text.strip()
        Logger.info(f"Текст сообщения: '{text}'")
        return text
