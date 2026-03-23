from selenium.common.exceptions import TimeoutException, NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser.browser import Browser
from pages.base_page import BasePage
from elements.button import Button
from elements.body import Body


class FramesPage(BasePage):

    NESTED_FRAMES = "//span[text()='Nested Frames']"
    FRAMES = "//span[text()='Frames']"
    PARENT_FRAME = "frame1"
    PARENT_FRAME_TEXT = "//body[contains(text(), 'Parent frame')]"
    CHILD_FRAME_TEXT = "//p[contains(text(), 'Child Iframe')]"
    TOP_FRAME = "frame1"
    BOTTOM_FRAME = "frame2"

    def __init__(self, browser: Browser):
        self.nested_frames_button = Button(browser, self.NESTED_FRAMES, description="Пункт меню 'Nested Frames'")
        self.frames_button = Button(browser, self.FRAMES, description="Пункт меню 'Frames'")
        unique = Button(browser, self.NESTED_FRAMES, description="Пункт меню 'Nested Frames'")
        super().__init__(browser, unique_element=unique, name="FramesPage")

    def click_nested_frames(self):
        self.nested_frames_button.click()

    def click_frames(self):
        self.frames_button.click()

    def is_parent_frame_present(self) -> bool:
        try:
            self.browser.switch_to_frame(self.PARENT_FRAME)
            element = Body(self.browser, self.PARENT_FRAME_TEXT, description="Parent frame")
            element.wait_for_visible()
            self.browser.switch_to_default_content()
            return True
        except TimeoutException:
            self.browser.switch_to_default_content()
            return False

    def is_child_frame_present(self) -> bool:
        try:
            self.browser.switch_to_frame(self.PARENT_FRAME)

            child_iframe = WebDriverWait(self.browser.driver, self.browser.DEFAULT_TIMEOUT).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            self.browser.switch_to_frame(child_iframe)

            element = Body(self.browser, self.CHILD_FRAME_TEXT, description="Child Iframe")
            element.wait_for_visible()
            self.browser.switch_to_default_content()
            return True
        except (TimeoutException, NoSuchFrameException):
            self.browser.switch_to_default_content()
            return False

    def switch_to_top_frame(self):
        self.browser.switch_to_frame(self.TOP_FRAME)

    def switch_to_bottom_frame(self):
        self.browser.switch_to_frame(self.BOTTOM_FRAME)

    def get_top_frame_text(self) -> str:
        self.switch_to_top_frame()
        body = Body(self.browser, "//body", description="Текст верхнего фрейма")
        text = body.get_text()
        self.browser.switch_to_default_content()
        return text

    def get_bottom_frame_text(self) -> str:
        self.switch_to_bottom_frame()
        body = Body(self.browser, "//body", description="Текст нижнего фрейма")
        text = body.get_text()
        self.browser.switch_to_default_content()
        return text
