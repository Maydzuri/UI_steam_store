from selenium.webdriver.support.ui import WebDriverWait
from browser.browser import Browser
from pages.base_page import BasePage
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from utils.logger import Logger


class InfiniteScrollPage(BasePage):

    PARAGRAPHS = "//div[contains(@class, 'jscroll-added')][{}]"
    PAGE_TITLE = "//h3[text()='Infinite Scroll']"

    def __init__(self, browser: Browser):
        self.paragraphs = MultiWebElement(browser, self.PARAGRAPHS, description="Абзац")
        title_element = WebElement(browser, self.PAGE_TITLE, description="Заголовок страницы")
        super().__init__(browser, unique_element=title_element, name="InfiniteScrollPage")

    def get_paragraph_count(self) -> int:
        count = 0
        for _ in self.paragraphs:
            count += 1
        Logger.info(f"Количество абзацев: {count}")
        return count

    def scroll_to_bottom(self):
        Logger.info("Прокрутка страницы вниз")
        self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_paragraphs_increase(self, old_count: int, timeout: int = None):
        timeout = timeout or self.browser.DEFAULT_TIMEOUT
        Logger.info(f"Ожидание увеличения количества абзацев (было {old_count})")

        WebDriverWait(self.browser.driver, timeout).until(
            lambda d: self._get_current_count() > old_count
        )

    def _get_current_count(self) -> int:
        count = 0
        for _ in self.paragraphs:
            count += 1
        return count
