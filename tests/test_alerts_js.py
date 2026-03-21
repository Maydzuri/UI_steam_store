import pytest
import random
import string
from pages.alerts_page import AlertsPage


class TestAlertsJS:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        browser.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.page = AlertsPage(browser)
        self.page.wait_for_open()

    def test_js_alert_js_click(self, browser):
        self.page.click_alert_js()
        alert_text = browser.accept_alert()
        assert alert_text == "I am a JS Alert"
        result = self.page.get_result_text()
        assert result == "You successfully clicked an alert"

    def test_js_confirm_ok_js_click(self, browser):
        self.page.click_confirm_js()
        alert_text = browser.accept_alert()
        assert alert_text == "I am a JS Confirm"
        result = self.page.get_result_text()
        assert result == "You clicked: Ok"

    def test_js_confirm_cancel_js_click(self, browser):
        self.page.click_confirm_js()
        alert_text = browser.dismiss_alert()
        assert alert_text == "I am a JS Confirm"
        result = self.page.get_result_text()
        assert result == "You clicked: Cancel"

    def test_js_prompt_js_click(self, browser):
        random_text = ''.join(random.choices(string.ascii_letters, k=10))
        self.page.click_prompt_js()
        alert_text = browser.wait_for_alert().text
        assert alert_text == "I am a JS prompt"
        browser.send_keys_to_alert(random_text)
        result = self.page.get_result_text()
        expected = f"You entered: {random_text}"
        assert result == expected
