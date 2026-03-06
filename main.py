from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://store.steampowered.com/?l=russian")

button_entrance = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'global_action_link')]")))
button_entrance.click()

name_field = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[contains(@class, '_2GBWeup5cttgbTw8FM3tfx') and @type='text']")))
name_field.click()
name_field.send_keys("Name")

password_field = browser.find_element(By.XPATH,
                                      "//input[contains(@class, '_2GBWeup5cttgbTw8FM3tfx') and @type='password']")
password_field.click()
password_field.send_keys("Password")

login_button = browser.find_element(By.XPATH, "//button[contains(@class, 'DjSvCZoKKfoNSmarsEcTS')]")
login_button.click()

error = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, '_1W_6HXiG4JJ0By1qN_0fGZ')]")))
