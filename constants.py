BROWSER_WIDTH = 1920
BROWSER_HEIGHT = 1080
TIMEOUT = 20
BASE_URL = "https://store.steampowered.com/"
SEARCH_LOCATOR = "//input[@placeholder = 'Поиск по магазину']"
ENTRANCE_LOCATOR = "//a[contains(@class, 'global_action_link')]"
NAME_LOCATOR = "(//input[@type='text' and @value=''])[2]"
PASSWORD_LOCATOR = "//input[@type='password']"
LOGIN_LOCATOR  = "(//button[@type='submit'])[2]"
ERROR_LOCATOR = "//div[contains(text(), 'Пожалуйста, проверьте')]"
ERROR_MESSAGE = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
