from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from browser.browser import Browser
from pages.base_page import BasePage
from elements.hot_spot import HotSpot


class ContextMenuPage(BasePage):

    HOT_SPOT_LOCATOR = "hot-spot"

    def __init__(self, browser: Browser):
        self.hot_spot = HotSpot(
            browser,
            self.HOT_SPOT_LOCATOR,
            description="Область для клика правой кнопкой мыши"
        )
        super().__init__(browser, unique_element=self.hot_spot, name="ContextMenuPage")

    def right_click_hot_spot(self):
        self.hot_spot.context_click()
