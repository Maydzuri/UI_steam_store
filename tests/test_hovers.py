from utils.logger import Logger


class TestHovers:

    def test_hovers(self, browser, hovers_page):
        page = hovers_page

        for i in range(3):
            Logger.info(f"=== Тестирование пользователя {i + 1} ===")

            page.hover_over_user(i)

            name = page.get_user_name(i)
            expected_name = f"name: user{i + 1}"
            assert name == expected_name, \
                f"Ожидалось имя '{expected_name}', получено '{name}'"

            page.click_profile_link(i)

            expected_url = f"https://the-internet.herokuapp.com/users/{i + 1}"
            browser.wait_for_url(expected_url)

            browser.back()
            page.wait_for_open()
