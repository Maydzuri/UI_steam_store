from selenium.common.exceptions import NoSuchWindowException
from browser.browser import Browser
from pages.base_page import BasePage
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from utils.logger import Logger


class DynamicContentPage(BasePage):
    IMAGES = "(//div[contains(@class, 'large-2 columns')]//img)[{}]"
    PAGE_TITLE = "//h3[text()='Dynamic Content']"

    def __init__(self, browser: Browser):
        self.images = MultiWebElement(browser, self.IMAGES, description="Изображение")
        title_element = WebElement(browser, self.PAGE_TITLE, description="Заголовок страницы")
        super().__init__(browser, unique_element=title_element, name="DynamicContentPage")

    def get_image_srcs(self) -> list:
        try:
            self.wait_for_open()
            srcs = []
            for img in self.images:
                srcs.append(img.get_attribute("src"))
            Logger.info(f"Получены src изображений: {srcs}")
            return srcs
        except NoSuchWindowException:
            Logger.error("Окно закрыто, возвращаем пустой список")
            return []

    def has_duplicate_images(self) -> bool:
        srcs = self.get_image_srcs()
        if not srcs:
            return False
        unique_count = len(set(srcs))
        total_count = len(srcs)
        Logger.info(f"Уникальных изображений: {unique_count}, всего: {total_count}")
        return unique_count < total_count
