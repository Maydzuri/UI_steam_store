from browser.browser import Browser
from utils.logger import Logger


class BasePage:
    def __init__(self, browser: Browser, name: str = None):
        self.browser = browser
        self.name = name or self.__class__.__name__

    def __str__(self):
        return f"{self.name}"

    def wait_for_open(self, timeout: int = None):
        Logger.info(f"{self}: ожидание открытия")
        pass
