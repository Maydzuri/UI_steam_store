from browser.browser import Browser
from pages.base_page import BasePage
from elements.slider import Slider
from elements.label import Label


class HorizontalSliderPage(BasePage):
    SLIDER_LOCATOR = "//input[@type='range']"
    VALUE_LOCATOR = "range"

    def __init__(self, browser: Browser):
        self.slider = Slider(browser, self.SLIDER_LOCATOR, description="Горизонтальный слайдер")
        self.value_label = Label(browser, self.VALUE_LOCATOR, description="Отображаемое значение")
        super().__init__(browser, unique_element=self.slider, name="HorizontalSliderPage")

    def get_current_value(self) -> float:
        value_str = self.value_label.get_text()
        return float(value_str)
