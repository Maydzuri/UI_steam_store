from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from constants import (
    BROWSER_WIDTH, BROWSER_HEIGHT, TIMEOUT, BASE_URL,
    SEARCH_LOCATOR, ENTRANCE_LOCATOR, NAME_LOCATOR,
    PASSWORD_LOCATOR, LOGIN_LOCATOR, ERROR_MESSAGE, ERROR_LOCATOR
)


fake = Faker()


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={BROWSER_WIDTH},{BROWSER_HEIGHT}")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(BASE_URL)
    yield browser
    browser.quit()


class TestLogin:
    def test_steam(self, browser):
        WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, SEARCH_LOCATOR)))

        button_entrance = WebDriverWait(browser, TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, ENTRANCE_LOCATOR)))
        button_entrance.click()

        name_field = WebDriverWait(browser, TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, NAME_LOCATOR)))
        name_field.send_keys(fake.name())

        password_field = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, PASSWORD_LOCATOR)))
        password_field.send_keys(fake.password())

        login_button = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, LOGIN_LOCATOR)))
        login_button.click()

        error_element = WebDriverWait(browser, TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, ERROR_LOCATOR))
        )
        assert ERROR_MESSAGE in error_element.text
