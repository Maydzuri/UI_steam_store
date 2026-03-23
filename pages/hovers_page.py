from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser.browser import Browser
from pages.base_page import BasePage
from elements.base_element import BaseElement
from elements.user_card import UserCard
from utils.logger import Logger


class HoversPage(BasePage):

    USER_CARDS = "//div[contains(@class, 'figure')]"
    USER_NAME = ".//h5"
    PROFILE_LINK = ".//a"

    def __init__(self, browser: Browser):
        first_card = UserCard(browser, self.USER_CARDS, description="Первая карточка пользователя")
        super().__init__(browser, unique_element=first_card, name="HoversPage")

    def _get_user_card(self, index: int):
        locator = f"({self.USER_CARDS})[{index + 1}]"
        return UserCard(self.browser, locator, description=f"Карточка пользователя {index + 1}")

    def hover_over_user(self, index: int):
        card = self._get_user_card(index)
        element = card.wait_for_visible()
        Logger.info(f"Наведение на карточку пользователя {index + 1}")
        ActionChains(self.browser.driver).move_to_element(element).perform()
        WebDriverWait(self.browser.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, f"({self.USER_CARDS})[{index + 1}]//h5"))
        )

    def get_user_name(self, index: int) -> str:
        name_element = BaseElement(self.browser, f"({self.USER_CARDS})[{index + 1}]//h5", description=f"Имя пользователя {index + 1}")
        return name_element.get_text()

    def click_profile_link(self, index: int):
        link_locator = f"({self.USER_CARDS})[{index + 1}]//a"
        link = BaseElement(self.browser, link_locator, description=f"Ссылка профиля {index + 1}")
        Logger.info(f"Клик по ссылке профиля пользователя {index + 1}")
        link.wait_for_clickable()
        link.click()
