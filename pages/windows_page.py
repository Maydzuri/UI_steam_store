from selenium.common.exceptions import TimeoutException
from browser.browser import Browser
from pages.base_page import BasePage
from elements.button import Button
from elements.label import Label


class WindowsPage(BasePage):

    CLICK_HERE_LINK = "//a[text()='Click Here']"
    NEW_WINDOW_TEXT = "//h3[text()='New Window']"

    def __init__(self, browser: Browser):
        self.click_here = Button(browser, self.CLICK_HERE_LINK, description="Ссылка 'Click Here'")
        self.new_window_label = Label(browser, self.NEW_WINDOW_TEXT, description="Заголовок 'New Window'")
        super().__init__(browser, unique_element=self.click_here, name="WindowsPage")

    def is_new_window_text_present(self, timeout: int = 2) -> bool:
        try:
            self.new_window_label.wait_for_visible(timeout)
            return True
        except TimeoutException:
            return False
