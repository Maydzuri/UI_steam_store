from selenium.webdriver.common.keys import Keys
from elements.input import Input
from utils.logger import Logger


class Slider(Input):

    def get_min(self) -> float:
        return float(self.get_attribute("min"))

    def get_max(self) -> float:
        return float(self.get_attribute("max"))

    def get_step(self) -> float:
        return float(self.get_attribute("step"))

    def get_current_value(self) -> float:
        return float(self.get_attribute("value"))

    def set_value_via_keys(self, value: float):
        current = self.get_current_value()
        if abs(current - value) < 0.01:
            return

        step = self.get_step()
        steps = int((value - current) / step)
        key = Keys.RIGHT if steps > 0 else Keys.LEFT

        self.click()
        self.send_keys(key * abs(steps))
        Logger.info(f"Установлено значение {value} (было {current}, шагов {abs(steps)})")
