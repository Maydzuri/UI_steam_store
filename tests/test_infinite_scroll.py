from utils.logger import Logger


class TestInfiniteScroll:

    ENGINEER_AGE = 29

    def test_infinite_scroll(self, infinite_scroll_page):
        page = infinite_scroll_page
        target = self.ENGINEER_AGE
        MAX_SCROLLS = 50

        Logger.info(f"Целевое количество абзацев: {target}")

        for scroll_count in range(1, MAX_SCROLLS + 1):
            current = page.get_paragraph_count()
            Logger.info(f"Прокрутка #{scroll_count}, текущее количество: {current}")

            if current >= target:
                Logger.info(f"Достигнуто целевое количество абзацев ({current})")
                return

            page.scroll_to_bottom()
            page.wait_for_paragraphs_increase(current)

        raise AssertionError(
            f"Не удалось достичь {target} абзацев после {MAX_SCROLLS} прокруток. "
            f"Последнее количество: {page.get_paragraph_count()}"
        )
