from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from browser.browser import Browser
from pages.base_page import BasePage
from elements.base_element import BaseElement


class ContextMenuPage(BasePage):

    HOT_SPOT_LOCATOR = (By.ID, "hot-spot")

    def __init__(self, browser: Browser):
        self.hot_spot = BaseElement(
            browser,
            self.HOT_SPOT_LOCATOR,
            description="Область для клика"
        )
        super().__init__(browser, unique_element=self.hot_spot, name="ContextMenuPage")

    def right_click(self):
        element = self.hot_spot.wait_for_presence()
        self.browser.context_click(element)
