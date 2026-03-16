from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ConfigReader import ConfigReader

config = ConfigReader()


class Browser:
    _current_driver = None
    _current_language = None

    def get_driver(self, language):
        if Browser._current_driver is None or Browser._current_language != language:
            if Browser._current_driver:
                Browser._current_driver.quit()
                Browser._current_driver = None

            Browser._current_driver = self._create_driver(language)
            Browser._current_language = language

        return Browser._current_driver

    def _create_driver(self, language):
        options = Options()
        options.add_argument(f"--lang={language}")
        options.add_argument(f"--window-size={config.get('WINDOW_WIDTH')},{config.get('WINDOW_HEIGHT')}")
        return webdriver.Chrome(options=options)

    def quit(self):
        if Browser._current_driver:
            Browser._current_driver.quit()
            Browser._current_driver = None
            Browser._current_language = None
