from selenium.common.exceptions import WebDriverException
from elements.base_element import BaseElement
from utils.logger import Logger


class Input(BaseElement):
    def clear(self, timeout: int = None):
        element = self.wait_for_visible(timeout)
        Logger.info(f"{self}: очистка поля")
        try:
            element.clear()
        except WebDriverException as e:
            Logger.error(f"{self}: ошибка очистки - {e}")
            raise

    def send_keys(self, keys: str, clear_first: bool = True, timeout: int = None):
        if clear_first:
            self.clear(timeout)
        element = self.wait_for_visible(timeout)
        Logger.info(f"{self}: ввод '{keys}'")
        try:
            element.send_keys(keys)
        except WebDriverException as e:
            Logger.error(f"{self}: ошибка ввода - {e}")
            raise

    def get_value(self, timeout: int = None) -> str:
        return self.get_attribute("value", timeout)
