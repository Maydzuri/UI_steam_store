from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from browser.browser_factory import BrowserFactory, AvailableDriverName
from utils.logger import Logger


class Browser:
    DEFAULT_TIMEOUT = 15

    def __init__(
        self,
        driver_name: AvailableDriverName = AvailableDriverName.CHROME,
        options: list[str] = None
    ):
        self.driver = BrowserFactory.get_driver(driver_name, options)
        Logger.info("Браузер инициализирован")

    def _ensure_driver(self):
        if not self.driver:
            raise RuntimeError("Браузер не инициализирован")

    def quit(self):
        self._ensure_driver()
        Logger.info("Закрытие браузера")
        self.driver.quit()
        self.driver = None

    def get(self, url: str):
        self._ensure_driver()
        Logger.info(f"Переход на {url}")
        self.driver.get(url)

    @property
    def title(self):
        self._ensure_driver()
        return self.driver.title

    @property
    def current_url(self):
        self._ensure_driver()
        return self.driver.current_url
