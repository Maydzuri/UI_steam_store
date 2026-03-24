from selenium.webdriver.common.keys import Keys
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

    def set_value_via_keys(self, value: float):
        current = self.get_current_value()
        if abs(current - value) < 0.01:
            return

        step = float(self.slider.get_attribute("step"))
        steps = int((value - current) / step)
        key = Keys.RIGHT if steps > 0 else Keys.LEFT

        self.slider.click()
        self.slider.send_keys(key * abs(steps))
