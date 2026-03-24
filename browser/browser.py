from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser.browser_factory import BrowserFactory, AvailableDriverName
from utils.logger import Logger
from elements.base_element import BaseElement


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
        Logger.info("Принятие алерта после ввода текста")
        alert.accept()

    def back(self):
        Logger.info("Возврат на предыдущую страницу")
        self.driver.back()

    @property
    def window_handles(self):
        return self.driver.window_handles

    @property
    def current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window(self, handle):
        Logger.info(f"Переключение на вкладку {handle}")
        self.driver.switch_to.window(handle)

    def close_current_window(self):
        Logger.info("Закрытие текущей вкладки")
        self.driver.close()

    def wait_for_new_window(self, old_handles, timeout: int = None):
        timeout = timeout or self.DEFAULT_TIMEOUT
        Logger.info(f"Ожидание появления новой вкладки (было {len(old_handles)} вкладок)")
        WebDriverWait(self.driver, timeout).until(
            EC.new_window_is_opened(old_handles)
        )
        new_handles = [h for h in self.window_handles if h not in old_handles]
        return new_handles[0]

    def switch_to_frame(self, frame_element: BaseElement, timeout: int = None):
        Logger.info(f"Переключение во фрейм: {frame_element}")
        element = frame_element.wait_for_presence(timeout)
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        Logger.info("Возврат в основной документ")
        self.driver.switch_to.default_content()

    def wait_for_url(self, expected_url: str, timeout: int = None):
        timeout = timeout or self.DEFAULT_TIMEOUT
        Logger.info(f"Ожидание URL: {expected_url}")
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url == expected_url
        )
