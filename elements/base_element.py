from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

from browser.browser import Browser
from utils.logger import Logger


class BaseElement:
    def __init__(self, browser: Browser, locator, description: str = ""):
        self.browser = browser
        self.description = description or str(locator)

        if isinstance(locator, str):
            if "/" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

    def __str__(self):
        return f"{self.__class__.__name__}({self.description})"

    def _wait_for(self, expected_condition, timeout: int = None):
        timeout = timeout or self.browser.DEFAULT_TIMEOUT
        try:
            Logger.info(f"{self}: ожидание {expected_condition.__name__}")
            element = WebDriverWait(self.browser.driver, timeout).until(
                expected_condition(self.locator)
            )
            return element
        except TimeoutException:
            Logger.error(f"{self}: не дождались {expected_condition.__name__} за {timeout}с")
            raise

    def wait_for_presence(self, timeout: int = None):
        return self._wait_for(EC.presence_of_element_located, timeout)

    def wait_for_visible(self, timeout: int = None):
        return self._wait_for(EC.visibility_of_element_located, timeout)

    def wait_for_clickable(self, timeout: int = None):
        return self._wait_for(EC.element_to_be_clickable, timeout)

    def get_text(self, timeout: int = None) -> str:
        Logger.info(f"{self}: получение текста")
        element = self.wait_for_visible(timeout)
        text = element.text.strip()
        Logger.info(f"{self}: текст = '{text}'")
        return text

    def click(self, timeout: int = None):
        element = self.wait_for_clickable(timeout)
        Logger.info(f"{self}: клик")
        try:
            element.click()
        except WebDriverException as e:
            Logger.error(f"{self}: ошибка клика - {e}")
            raise

    def click_via_js(self, timeout: int = None):
        element = self.wait_for_presence(timeout)
        Logger.info(f"{self}: JS-клик")
        self.browser.driver.execute_script("arguments[0].click();", element)

    def context_click(self, timeout: int = None):
        element = self.wait_for_presence(timeout)
        Logger.info(f"{self}: контекстный клик")
        ActionChains(self.browser.driver).context_click(element).perform()

    def send_keys(self, keys: str, timeout: int = None):
        element = self.wait_for_visible(timeout)
        Logger.info(f"{self}: отправка клавиш '{keys}'")
        try:
            element.send_keys(keys)
        except WebDriverException as e:
            Logger.error(f"{self}: ошибка отправки клавиш - {e}")
            raise
