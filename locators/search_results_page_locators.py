from selenium.webdriver.common.by import By


class SearchResultsPageLocators:
    SORT_DROPDOWN = (By.XPATH, "//*[@id='sort_by_trigger']")
    SORT_PRICE_DESC = (By.XPATH, "//*[@id='Price_DESC']")
    GAME_ROWS = (By.XPATH, "//a[contains(@class, 'search_result_row')]")
    GAME_PRICE = (By.XPATH, "//div[contains(@class, 'discount_final_price') or contains(@class, 'game_purchase_price')]")

