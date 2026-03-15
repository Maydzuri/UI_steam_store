from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIMEOUT, POLL_FREQUENCY
from locators.search_results_page_locators import SearchResultsPageLocators


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT, POLL_FREQUENCY)
        self.locators = SearchResultsPageLocators

    def set_sort_by_price_desc(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.locators.SORT_DROPDOWN))
        dropdown.click()

        option = self.wait.until(EC.element_to_be_clickable(self.locators.SORT_PRICE_DESC))
        option.click()

        self.wait.until(EC.presence_of_element_located(self.locators.GAME_ROWS))

    def get_first_n_games(self, n):
        all_games = self.wait.until(EC.presence_of_all_elements_located(self.locators.GAME_ROWS))
        return all_games[:n]

    def get_game_prices(self, games):
        prices = []
        for game in games:
            try:
                price_element = game.find_element(*self.locators.GAME_PRICE)
                price_text = price_element.text.replace(" pуб.", "").replace("$", "").replace(",", ".")
                prices.append(float(price_text) if price_text else 0.0)
            except:
                prices.append(0.0)
        return prices