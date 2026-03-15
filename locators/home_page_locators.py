from selenium.webdriver.common.by import By


class HomePageLocators:
    SEARCH_BOX = (By.XPATH, "//input[@role='combobox']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
