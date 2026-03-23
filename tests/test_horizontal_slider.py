import random
from utils.logger import Logger


class TestHorizontalSlider:

    def test_slider_set_value(self, slider_page):
        page = slider_page

        possible_values = [x * 0.5 for x in range(1, 10)]
        target = random.choice(possible_values)
        Logger.info(f"Целевое значение: {target}")

        page.set_value_via_keys(target)

        actual = page.get_current_value()
        assert actual == target, \
            f"Ожидалось значение '{target}', получено '{actual}'"