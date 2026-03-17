from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ConfigReader import ConfigReader
from browser import Browser

config = ConfigReader()


class HomePage:

    SEARCH_BOX = (By.XPATH, "//input[@role='combobox']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self):
        self.driver = Browser.get_driver()
        self.wait = WebDriverWait(
            self.driver,
            config.get('TIMEOUT'),
            config.get('POLL_FREQUENCY')
        )

    def wait_for_page_to_load(self):
        self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))

    def search(self, game_name):
        search_box = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX))
        search_box.clear()
        search_box = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX))
        search_box.send_keys(game_name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()
