from browser.browser import Browser
from pages.dynamic_content_page import DynamicContentPage
from utils.logger import Logger


class TestDynamicContent:

    def test_dynamic_content(self):
        MAX_ATTEMPTS = 20

        for attempt in range(1, MAX_ATTEMPTS + 1):
            Logger.info(f"Попытка #{attempt}: загрузка страницы")

            browser = Browser()
            try:
                browser.get("https://the-internet.herokuapp.com/dynamic_content")
                browser.wait_for_page_load()
                page = DynamicContentPage(browser)
                page.wait_for_open()

                srcs = page.get_image_srcs()
                print(f"\nПопытка {attempt}: {srcs}")  # ← добавить сюда

                if page.has_duplicate_images():
                    Logger.info(f"Найдено совпадение на попытке {attempt}")
                    browser.quit()
                    return

            except Exception as e:
                Logger.error(f"Ошибка в попытке #{attempt}: {e}")

            finally:
                browser.quit()

        raise AssertionError(f"Совпадение изображений не найдено за {MAX_ATTEMPTS} попыток")
