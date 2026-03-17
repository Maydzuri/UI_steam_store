from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ConfigReader import ConfigReader

config = ConfigReader()


class Browser:
    _instance = None
    _driver = None
    _current_language = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_driver(cls, language=None):
        if language is not None and (cls._driver is None or cls._current_language != language):
            if cls._driver:
                cls._driver.quit()
                cls._driver = None

            cls._driver = cls._create_driver(language)
            cls._current_language = language

        if cls._driver is None:
            default_language = "en"  # можно вынести в конфиг
            cls._driver = cls._create_driver(default_language)
            cls._current_language = default_language

        return cls._driver

    @classmethod
    def _create_driver(cls, language):
        options = Options()
        options.add_argument(f"--lang={language}")
        options.add_argument(f"--window-size={config.get('WINDOW_WIDTH')},{config.get('WINDOW_HEIGHT')}")
        return webdriver.Chrome(options=options)

    @classmethod
    def quit(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
            cls._current_language = None
            cls._instance = None
