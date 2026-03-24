from selenium.webdriver.common.by import By
from browser.browser import Browser
from pages.base_page import BasePage
from elements.web_element import WebElement
from utils.logger import Logger


class DynamicContentPage(BasePage):

    IMAGES = "//div[@class='large-2 columns']//img"
    PAGE_TITLE = "//h3[text()='Dynamic Content']"

    def __init__(self, browser: Browser):
        title_element = WebElement(browser, self.PAGE_TITLE, description="Заголовок страницы")
        super().__init__(browser, unique_element=title_element, name="DynamicContentPage")

    def get_image_srcs(self) -> list:
        images = self.browser.driver.find_elements(By.XPATH, self.IMAGES)
        srcs = [img.get_attribute("src") for img in images]
        Logger.info(f"Получены src изображений: {srcs}")
        return srcs

    def has_duplicate_images(self) -> bool:
        srcs = self.get_image_srcs()
        return len(set(srcs)) < len(srcs)

    def refresh_page(self):
        Logger.info("Обновление страницы")
        self.browser.refresh()
        self.wait_for_open()
