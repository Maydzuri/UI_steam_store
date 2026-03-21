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

    def quit(self):
        Logger.info("Закрытие браузера")
        self.driver.quit()
        self.driver = None

    def get(self, url: str):
        Logger.info(f"Переход на {url}")
        self.driver.get(url)

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url
