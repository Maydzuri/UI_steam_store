from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from enum import StrEnum
from ConfigReader import ConfigReader

config = ConfigReader()


class Language(StrEnum):
    RUSSIAN = "ru"
    ENGLISH = "en"


class Browser:
    _driver = None
    _current_language = None

    def __new__(cls, language: Language = None):
        if language is None and cls._current_language is not None:
            language = cls._current_language

        if language is None:
            language = Language.ENGLISH

        if cls._driver is None:
            options = Options()
            options.add_argument(f"--lang={language}")
            options.add_argument(f"--window-size={config.get('WINDOW_WIDTH')},{config.get('WINDOW_HEIGHT')}")
            cls._driver = webdriver.Chrome(options=options)
            cls._current_language = language
            return cls._driver

        if language != cls._current_language:
            cls._driver.quit()
            options = Options()
            options.add_argument(f"--lang={language}")
            options.add_argument(f"--window-size={config.get('WINDOW_WIDTH')},{config.get('WINDOW_HEIGHT')}")
            cls._driver = webdriver.Chrome(options=options)
            cls._current_language = language

        return cls._driver

    @classmethod
    def quit(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
            cls._current_language = None
