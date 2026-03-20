from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from browser.browser_factory import BrowserFactory, AvailableDriverName
from utils.logger import Logger


class Browser:
    def __init__(
        self,
        driver_name: AvailableDriverName = AvailableDriverName.CHROME,
        options: list[str] = None
    ):
        self.driver = BrowserFactory.get_driver(driver_name, options)
        self.default_timeout = 15
        Logger.info("Браузер инициализирован")

    def quit(self):
        if self.driver:
            Logger.info("Закрытие браузера")
            self.driver.quit()

    def get(self, url: str):
        Logger.info(f"Переход на {url}")
        self.driver.get(url)

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text: str, timeout: int = None):
        timeout = timeout or self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
        except TimeoutException:
            Logger.error(f"URL не содержит '{text}' после {timeout}с")
            raise
