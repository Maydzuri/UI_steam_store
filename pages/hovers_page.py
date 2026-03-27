from selenium.webdriver.common.action_chains import ActionChains
from browser.browser import Browser
from pages.base_page import BasePage
from elements.label import Label
from elements.web_element import WebElement
from utils.logger import Logger


class HoversPage(BasePage):
    USER_CARDS = "//div[contains(@class, 'figure')]"
    USER_NAME_TEMPLATE = "({})[{}]//h5"
    PROFILE_LINK_TEMPLATE = "({})[{}]//a"
    PAGE_TITLE = "//h3[text()='Hovers']"

    def __init__(self, browser: Browser):
        title_element = Label(browser, self.PAGE_TITLE, description="Заголовок страницы")
        super().__init__(browser, unique_element=title_element, name="HoversPage")

    def _get_user_card(self, index: int):
        locator = f"({self.USER_CARDS})[{index + 1}]"
        return WebElement(self.browser, locator, description=f"Карточка пользователя {index + 1}")

    def _get_name_locator(self, index: int) -> str:
        return self.USER_NAME_TEMPLATE.format(self.USER_CARDS, index + 1)

    def _get_link_locator(self, index: int) -> str:
        return self.PROFILE_LINK_TEMPLATE.format(self.USER_CARDS, index + 1)

    def hover_over_user(self, index: int, timeout: int = None):
        card = self._get_user_card(index)
        element = card.wait_for_visible(timeout)
        Logger.info(f"Наведение на карточку пользователя {index + 1}")
        ActionChains(self.browser.driver).move_to_element(element).perform()

        name_locator = self._get_name_locator(index)
        name_element = WebElement(self.browser, name_locator, description=f"Имя пользователя {index + 1}")
        name_element.wait_for_visible(timeout)

    def get_user_name(self, index: int) -> str:
        name_locator = self._get_name_locator(index)
        name_element = Label(self.browser, name_locator, description=f"Имя пользователя {index + 1}")
        return name_element.get_text()

    def click_profile_link(self, index: int):
        link_locator = self._get_link_locator(index)
        link = WebElement(self.browser, link_locator, description=f"Ссылка профиля {index + 1}")
        link.click()
