from utils.logger import Logger


class TestFramesPage:

    def test_nested_frames_and_frames(self, browser, frames_page):
        page = frames_page

        page.click_nested_frames()

        assert page.is_parent_frame_present(), \
            "Текст 'Parent frame' не найден на странице Nested Frames"
        Logger.info("Текст 'Parent frame' найден")

        assert page.is_child_frame_present(), \
            "Текст 'Child Iframe' не найден на странице Nested Frames"
        Logger.info("Текст 'Child Iframe' найден")

        browser.get("https://demoqa.com/frames")
        page.wait_for_open()
        page.click_frames()

        top_text = page.get_top_frame_text()
        bottom_text = page.get_bottom_frame_text()

        Logger.info(f"Текст верхнего фрейма: {top_text}")
        Logger.info(f"Текст нижнего фрейма: {bottom_text}")

        assert top_text == bottom_text, \
            f"Текст верхнего фрейма '{top_text}' не совпадает с текстом нижнего '{bottom_text}'"
