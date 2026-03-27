import random
from utils.logger import Logger


class TestHorizontalSlider:

    def test_slider_set_value(self, slider_page):
        page = slider_page
        slider = page.slider

        min_val = slider.get_min()
        max_val = slider.get_max()
        step = slider.get_step()

        possible_values = []
        val = min_val
        while val <= max_val + 0.01:
            possible_values.append(val)
            val += step

        possible_values = [v for v in possible_values if v not in (min_val, max_val)]

        target = random.choice(possible_values)
        Logger.info(f"Целевое значение: {target}")

        slider.set_value_via_keys(target)

        actual = page.get_current_value()
        assert actual == target, \
            f"Ожидалось значение '{target}', получено '{actual}'"
