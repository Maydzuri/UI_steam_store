from browser.browser import Browser
from pages.base_page import BasePage
from elements.button import Button
from elements.body import Body
from elements.web_element import WebElement


class FramesPage(BasePage):

    NESTED_FRAMES = "//span[text()='Nested Frames']"
    FRAMES = "//span[text()='Frames']"
    PARENT_FRAME_LOCATOR = "frame1"
    CHILD_FRAME_LOCATOR = ".//iframe"
    PARENT_FRAME_TEXT = "//body[contains(text(), 'Parent frame')]"
    CHILD_FRAME_TEXT = "//p[contains(text(), 'Child Iframe')]"
    TOP_FRAME_LOCATOR = "frame1"
    BOTTOM_FRAME_LOCATOR = "frame2"
    BODY_LOCATOR = "//body"

    def __init__(self, browser: Browser):
        self.nested_frames_button = Button(browser, self.NESTED_FRAMES, description="Пункт меню 'Nested Frames'")
        self.frames_button = Button(browser, self.FRAMES, description="Пункт меню 'Frames'")
        unique = Button(browser, self.NESTED_FRAMES, description="Пункт меню 'Nested Frames'")
        super().__init__(browser, unique_element=unique, name="FramesPage")

        self.parent_frame_element = WebElement(browser, self.PARENT_FRAME_LOCATOR, description="Родительский фрейм")
        self.parent_text = Body(browser, self.PARENT_FRAME_TEXT, description="Parent frame")
        self.child_text = Body(browser, self.CHILD_FRAME_TEXT, description="Child Iframe")

        self.top_frame = WebElement(browser, self.TOP_FRAME_LOCATOR, description="Верхний фрейм")
        self.bottom_frame = WebElement(browser, self.BOTTOM_FRAME_LOCATOR, description="Нижний фрейм")
        self.body = Body(browser, self.BODY_LOCATOR, description="Текст внутри фрейма")

    def click_nested_frames(self):
        self.nested_frames_button.click()

    def click_frames(self):
        self.frames_button.click()

    def is_parent_frame_present(self) -> bool:
        if not self.parent_frame_element.is_exists():
            return False

        self.browser.switch_to_frame(self.parent_frame_element)
        is_present = self.parent_text.is_exists()
        self.browser.switch_to_default_content()
        return is_present

    def is_child_frame_present(self) -> bool:
        if not self.parent_frame_element.is_exists():
            return False

        self.browser.switch_to_frame(self.parent_frame_element)

        child_frame = WebElement(self.browser, self.CHILD_FRAME_LOCATOR, description="Дочерний фрейм")
        if not child_frame.is_exists():
            self.browser.switch_to_default_content()
            return False

        self.browser.switch_to_frame(child_frame.wait_for_presence())

        is_present = self.child_text.is_exists()
        self.browser.switch_to_default_content()
        return is_present

    def get_top_frame_text(self) -> str:
        self.browser.switch_to_frame(self.top_frame)
        text = self.body.get_text()
        self.browser.switch_to_default_content()
        return text

    def get_bottom_frame_text(self) -> str:
        self.browser.switch_to_frame(self.bottom_frame)
        text = self.body.get_text()
        self.browser.switch_to_default_content()
        return text
