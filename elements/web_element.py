from elements.base_element import BaseElement


class WebElement(BaseElement):
    def __init__(self, browser, locator, description: str = ""):
        if hasattr(locator, 'tag_name'):
            self._cached_element = locator
            self.browser = browser
            self.description = description or str(locator)
            self.locator = None
            self._is_cached = True
        else:
            self._is_cached = False
            super().__init__(browser, locator, description)

    def _find_element(self, timeout: int = None):
        if self._is_cached:
            return self._cached_element
        return super()._find_element(timeout)

    def _wait_for(self, expected_condition, timeout: int = None):
        if self._is_cached:
            return self._cached_element
        return super()._wait_for(expected_condition, timeout)
