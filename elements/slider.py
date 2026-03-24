from elements.base_element import BaseElement


class Slider(BaseElement):

    def get_min(self) -> float:
        return float(self.get_attribute("min"))

    def get_max(self) -> float:
        return float(self.get_attribute("max"))

    def get_step(self) -> float:
        return float(self.get_attribute("step"))