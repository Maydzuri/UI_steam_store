import pytest
from utils.logger import Logger


class TestDynamicContent:

    def test_dynamic_content(self, dynamic_content_page):
        page = dynamic_content_page
        MAX_REFRESHES = 20

        for attempt in range(1, MAX_REFRESHES + 1):
            Logger.info(f"Попытка #{attempt}: проверка изображений")

            if page.has_duplicate_images():
                Logger.info(f"Найдено совпадение изображений после {attempt} обновлений")
                return

            page.refresh_page()

        pytest.fail(f"Не найдено совпадений изображений после {MAX_REFRESHES} обновлений")
