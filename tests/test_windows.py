from utils.logger import Logger


class TestWindows:

    def test_windows(self, browser, windows_page):
        page = windows_page
        main_handle = browser.current_window_handle
        Logger.info(f"Главная вкладка: {main_handle}")

        old_handles = browser.window_handles
        page.click_here.click()

        tab1_handle = browser.wait_for_new_window(old_handles)
        Logger.info(f"Первая новая вкладка: {tab1_handle}")

        browser.switch_to_window(tab1_handle)

        assert page.is_new_window_text_present(), \
            f"Ожидался текст 'New Window', но он не появился. " \
            f"Текущий URL: {browser.current_url}, заголовок: {browser.title}"

        browser.switch_to_window(main_handle)

        old_handles = browser.window_handles
        page.click_here.click()

        tab2_handle = browser.wait_for_new_window(old_handles)
        Logger.info(f"Вторая новая вкладка: {tab2_handle}")

        browser.switch_to_window(tab2_handle)

        assert page.is_new_window_text_present(), \
            f"Ожидался текст 'New Window', но он не появился. " \
            f"Текущий URL: {browser.current_url}, заголовок: {browser.title}"

        browser.switch_to_window(main_handle)

        Logger.info("Закрытие первой новой вкладки")
        browser.switch_to_window(tab1_handle)
        browser.close_current_window()

        Logger.info("Закрытие второй новой вкладки")
        browser.switch_to_window(tab2_handle)
        browser.close_current_window()

        browser.switch_to_window(main_handle)
        assert len(browser.window_handles) == 1, \
            f"Ожидалась 1 вкладка, осталось {len(browser.window_handles)}"
