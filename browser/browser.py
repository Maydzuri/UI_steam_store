from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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

    def get(self, url: str):
        Logger.info(f"Переход на {url}")
        self.driver.get(url)

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def wait_for_alert(self, timeout: int = None):
        timeout = timeout or self.DEFAULT_TIMEOUT
        Logger.info("Ожидание появления алерта")
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

    def accept_alert(self, timeout: int = None) -> str:
        alert = self.wait_for_alert(timeout)
        text = alert.text
        Logger.info(f"Принятие алерта с текстом: '{text}'")
        alert.accept()
        return text

    def dismiss_alert(self, timeout: int = None) -> str:
        alert = self.wait_for_alert(timeout)
        text = alert.text
        Logger.info(f"Отклонение алерта с текстом: '{text}'")
        alert.dismiss()
        return text

    def send_keys_to_alert(self, keys: str, timeout: int = None):
        alert = self.wait_for_alert(timeout)
        Logger.info(f"Ввод текста '{keys}' в алерт")
        alert.send_keys(keys)
        alert.accept()

    def context_click(self, element):
        Logger.info(f"Клик правой кнопкой мыши по элементу: {element}")
        ActionChains(self.driver).context_click(element).perform()
