from pages.dynamic_content_page import DynamicContentPage
from utils.logger import Logger


class TestDynamicContent:

    def test_dynamic_content(self, browser):
        MAX_ATTEMPTS = 20

        for attempt in range(1, MAX_ATTEMPTS + 1):
            Logger.info(f"Попытка #{attempt}: загрузка страницы")

            browser.get("https://the-internet.herokuapp.com/dynamic_content")
            browser.wait_for_page_load()
            page = DynamicContentPage(browser)
            page.wait_for_open()

            if page.has_duplicate_images():
                Logger.info(f"Найдено совпадение на попытке {attempt}")
                return

        raise AssertionError(f"Совпадение изображений не найдено за {MAX_ATTEMPTS} попыток")
