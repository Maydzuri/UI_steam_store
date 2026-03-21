from selenium.webdriver.common.by import By

from browser.browser import Browser
from pages.base_page import BasePage
from elements.button import Button
from elements.label import Label


class AlertsPage(BasePage):

    ALERT_BUTTON = (By.XPATH, "//button[@onclick='jsAlert()']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@onclick='jsConfirm()']")
    PROMPT_BUTTON = (By.XPATH, "//button[@onclick='jsPrompt()']")
    RESULT_TEXT = (By.ID, "result")

    def __init__(self, browser: Browser):
        self.alert_button = Button(browser, self.ALERT_BUTTON, description="Кнопка JS Alert")
        self.confirm_button = Button(browser, self.CONFIRM_BUTTON, description="Кнопка JS Confirm")
        self.prompt_button = Button(browser, self.PROMPT_BUTTON, description="Кнопка JS Prompt")
        self.result_label = Label(browser, self.RESULT_TEXT, description="Результат после закрытия алерта")

        super().__init__(browser, unique_element=self.alert_button, name="AlertsPage")

    def get_result_text(self) -> str:
        return self.result_label.get_text()

    def click_alert_js(self):
        self.alert_button.click_via_js()

    def click_confirm_js(self):
        self.confirm_button.click_via_js()

    def click_prompt_js(self):
        self.prompt_button.click_via_js()
