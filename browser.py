from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import WINDOW_WIDTH, WINDOW_HEIGHT


class Browser:
    _instance = None
    _current_driver = None
    _current_language = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_driver(self, language):
        if self._current_driver is None or self._current_language != language:
            if self._current_driver:
                self._current_driver.quit()
                self._current_driver = None

            self._current_driver = self._create_driver(language)
            self._current_language = language

        return self._current_driver

    def _create_driver(self, language):
        options = Options()
        options.add_argument(f"--lang={language}")
        options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")
        return webdriver.Chrome(options=options)

    def quit(self):
        if self._current_driver:
            self._current_driver.quit()
            self._current_driver = None
            self._current_language = None
            Browser._instance = None
