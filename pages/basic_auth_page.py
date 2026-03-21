from selenium.webdriver.common.by import By
from browser.browser import Browser
from pages.base_page import BasePage
from elements.base_element import BaseElement


class BasicAuthPage(BasePage):
    def __init__(self, browser: Browser):
        success_message_element = BaseElement(
            browser,
            (By.XPATH, "//div[contains(@class, 'example')]/p"),
            description="Сообщение об успехе"
        )

        super().__init__(browser, unique_element=success_message_element, name="BasicAuthPage")

        self.success_message = success_message_element

    def get_success_message(self) -> str:
        return self.success_message.get_text()
