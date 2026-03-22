from utils.logger import Logger


class TestContextMenu:
    def test_context_menu(self, browser, context_menu_page):
        page = context_menu_page
        page.right_click_hot_spot()

        alert_text = browser.accept_alert()
        Logger.info(f"Текст алерта: {alert_text}")

        assert alert_text == "You selected a context menu", \
            f"Ожидался текст 'You selected a context menu', получен '{alert_text}'"