from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from browser.browser import Browser
from utils.logger import Logger


class BaseElement:
    def __init__(self, browser: Browser, locator: tuple, description: str = ""):
        self.browser = browser
        self.locator = locator
        self.description = description or str(locator)

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
        element = self.wait_for_presence(timeout)
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
