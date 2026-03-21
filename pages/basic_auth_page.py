from selenium.webdriver.common.by import By
from browser.browser import Browser
from pages.base_page import BasePage
from elements.label import Label


class BasicAuthPage(BasePage):

    SUCCESS_MESSAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'example')]/p")

    def __init__(self, browser: Browser):
        self.success_message = Label(
            browser,
            self.SUCCESS_MESSAGE_LOCATOR,
            description="Сообщение об успехе"
        )

        super().__init__(browser, unique_element=self.success_message, name="BasicAuthPage")

    def get_success_message(self) -> str:
        return self.success_message.get_text()
