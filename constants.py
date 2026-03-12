from selenium.webdriver.common.by import By



BROWSER_WIDTH = 1920
BROWSER_HEIGHT = 1080
TIMEOUT = 20
BASE_URL = "https://store.steampowered.com/"
SEARCH_LOCATOR = (By.XPATH, "//input[@placeholder = 'Поиск по магазину']")
ENTRANCE_LOCATOR = (By.XPATH, "//a[contains(@class, 'global_action_link')]")
NAME_LOCATOR = (By.XPATH, "(//input[@type='text' and @value=''])[2]")
PASSWORD_LOCATOR = (By.XPATH, "//input[@type='password']")
LOGIN_LOCATOR  = (By.XPATH, "(//button[@type='submit'])[2]")
ERROR_LOCATOR = (By.XPATH, "(//button[@type='submit']/following::div[contains(@class, '')][1])[2]")
ERROR_MESSAGE = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
