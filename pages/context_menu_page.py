from browser.browser import Browser
from pages.base_page import BasePage
from elements.web_element import WebElement

class ContextMenuPage(BasePage):
    HOT_SPOT_LOCATOR = "hot-spot"

    def __init__(self, browser: Browser):
        self.hot_spot = WebElement(browser, self.HOT_SPOT_LOCATOR, description="Область для контекстного клика")
        super().__init__(browser, unique_element=self.hot_spot, name="ContextMenuPage")

    def right_click_hot_spot(self):
        self.hot_spot.context_click()
