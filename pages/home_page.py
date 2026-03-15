from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIMEOUT, POLL_FREQUENCY
from locators.home_page_locators import HomePageLocators
from locators.search_results_page_locators import SearchResultsPageLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT, POLL_FREQUENCY)
        self.locators = HomePageLocators

    def open(self, url):
        self.driver.get(url)
        self.driver.delete_all_cookies()
        self.wait.until(EC.presence_of_element_located(self.locators.SEARCH_BOX))

    def search(self, game_name):
        search_box = self.wait.until(EC.element_to_be_clickable(self.locators.SEARCH_BOX))
        search_box.clear()
        search_box.send_keys(game_name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.locators.SEARCH_BUTTON))
        search_button.click()

        self.wait.until(EC.presence_of_element_located(SearchResultsPageLocators.GAME_ROWS))