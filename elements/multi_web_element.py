from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.web_element import WebElement
from utils.logger import Logger


class MultiWebElement:
    def __init__(self, browser, locator: str, description: str = ""):
        self.browser = browser
        self.locator = locator
        self.description = description or locator

    def __str__(self):
        return f"{self.__class__.__name__}({self.description})"

    def wait_for_all_visible(self, timeout: int = None) -> List[WebElement]:
        timeout = timeout or self.browser.DEFAULT_TIMEOUT
        Logger.info(f"{self}: ожидание видимости всех элементов")

        raw_elements = WebDriverWait(self.browser.driver, timeout).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locator))
        )

        wrapped = []
        for i, raw in enumerate(raw_elements):
            wrapped.append(WebElement(self.browser, raw, description=f"{self.description}[{i}]"))

        Logger.info(f"Найдено {len(wrapped)} видимых элементов")
        return wrapped
