from enum import StrEnum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.logger import Logger


class AvailableDriverName(StrEnum):
    CHROME = "chrome"


class BrowserFactory:
    @staticmethod
    def get_driver(
            driver_name: AvailableDriverName = AvailableDriverName.CHROME,
            options: list[str] = None,
    ):
        if options is None:
            options = []

        Logger.info(f"Start webdriver '{driver_name}' with options '{options}'")

        if driver_name == AvailableDriverName.CHROME:
            chrome_options = Options()
            for option in options:
                chrome_options.add_argument(option)
            driver = webdriver.Chrome(options=chrome_options)
        else:
            raise NotImplementedError(f"({driver_name}) not implemented.")

        return driver
