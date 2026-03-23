from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

from browser.browser import Browser
from pages.base_page import BasePage
from elements.slider import Slider
from elements.label import Label
from utils.logger import Logger


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

        step = 0.5
        steps = int((value - current) / step)
        key = Keys.RIGHT if steps > 0 else Keys.LEFT

        self.slider.send_keys("")
        time.sleep(0.2)

        for _ in range(abs(steps)):
            self.slider.send_keys(key)
            time.sleep(0.1)

        self.wait_for_value(value)

    def wait_for_value(self, expected_value: float, timeout: int = None):
        timeout = timeout or 10
        Logger.info(f"Ожидание значения {expected_value}")
        WebDriverWait(self.browser.driver, timeout).until(
            lambda d: abs(self.get_current_value() - expected_value) < 0.01
        )
