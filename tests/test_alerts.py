import random
import string

from utils.logger import Logger


class TestAlerts:

    def test_js_alert(self, browser, alerts_page):
        page = alerts_page
        page.alert_button.click()
        alert_text = browser.accept_alert()
        assert alert_text == "I am a JS Alert", \
            f"Ожидался текст 'I am a JS Alert', получен '{alert_text}'"
        result = page.get_result_text()
        assert result == "You successfully clicked an alert", \
            f"Ожидался результат 'You successfully clicked an alert', получен '{result}'"

    def test_js_confirm_ok(self, browser, alerts_page):
        page = alerts_page
        page.confirm_button.click()
        alert_text = browser.accept_alert()
        assert alert_text == "I am a JS Confirm", \
            f"Ожидался текст 'I am a JS Confirm', получен '{alert_text}'"
        result = page.get_result_text()
        assert result == "You clicked: Ok", \
            f"Ожидался результат 'You clicked: Ok', получен '{result}'"

    def test_js_confirm_cancel(self, browser, alerts_page):
        page = alerts_page
        page.confirm_button.click()
        alert_text = browser.dismiss_alert()
        assert alert_text == "I am a JS Confirm", \
            f"Ожидался текст 'I am a JS Confirm', получен '{alert_text}'"
        result = page.get_result_text()
        assert result == "You clicked: Cancel", \
            f"Ожидался результат 'You clicked: Cancel', получен '{result}'"

    def test_js_prompt(self, browser, alerts_page):
        page = alerts_page
        random_text = ''.join(random.choices(string.ascii_letters, k=10))
        Logger.info(f"Сгенерированный текст: {random_text}")

        page.prompt_button.click()

        alert_text = browser.wait_for_alert().text
        assert alert_text == "I am a JS prompt", \
            f"Ожидался текст 'I am a JS prompt', получен '{alert_text}'"

        browser.send_keys_to_alert(random_text)

        result = page.get_result_text()
        expected = f"You entered: {random_text}"
        assert result == expected, \
            f"Ожидался результат '{expected}', получен '{result}'"
