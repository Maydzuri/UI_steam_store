from browser.browser import Browser
from elements.base_element import BaseElement
from utils.logger import Logger


class BasePage:
    def __init__(self, browser: Browser, unique_element: BaseElement = None, name: str = None):
        self.browser = browser
        self.name = name or self.__class__.__name__
        self.unique_element = unique_element

    def __str__(self):
        return f"{self.name}"

    def wait_for_open(self, timeout: int = None):
        if self.unique_element is None:
            raise NotImplementedError(
                f"{self.name}: unique_element не задан. Невозможно определить момент открытия страницы."
            )
        Logger.info(f"{self}: ожидание открытия")
        self.unique_element.wait_for_presence(timeout)
        Logger.info(f"{self}: открыта")