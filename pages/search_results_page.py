from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from ConfigReader import ConfigReader
from browser import Browser

config = ConfigReader()


class SearchResultsPage:
    SORT_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_PRICE_DESC = (By.ID, "Price_DESC")
    SORT_DROPDOWN_ACTIVE = (By.XPATH, "//button[@aria-activedescendant='Price_DESC']")
    GAME_ROWS = (By.XPATH, "//a[contains(@class, 'search_result_row')]")
    GAME_PRICE = (By.XPATH,
                  "//div[contains(@class, 'discount_final_price') or contains(@class, 'game_purchase_price')]")

    def __init__(self):
        self.driver = Browser.get_driver()
        self.wait = WebDriverWait(
            self.driver,
            config.get('TIMEOUT'),
            config.get('POLL_FREQUENCY')
        )

    def wait_for_page_to_load(self):
        self.wait.until(EC.presence_of_element_located(self.GAME_ROWS))

    def set_sort_by_price_desc(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN))
        dropdown.click()

        option = self.wait.until(EC.element_to_be_clickable(self.SORT_PRICE_DESC))
        option.click()

        self.wait.until(EC.presence_of_element_located(self.SORT_DROPDOWN_ACTIVE))
        self.wait.until(EC.presence_of_element_located(self.GAME_ROWS))

    def get_first_n_games(self, n):
        all_games = self.wait.until(EC.presence_of_all_elements_located(self.GAME_ROWS))
        return all_games[:n]

    def get_game_prices(self, games):
        prices = []
        for game in games:
            try:
                price_element = WebDriverWait(game, config.get('TIMEOUT')).until(
                    EC.visibility_of_element_located(self.GAME_PRICE)
                )
                price_text = price_element.text.replace(" pуб.", "").replace("$", "").replace(",", ".")
                prices.append(float(price_text) if price_text else 0.0)
            except TimeoutException:
                prices.append(0.0)
        return prices
