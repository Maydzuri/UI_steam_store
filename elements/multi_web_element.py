from typing_extensions import Self

from elements.web_element import WebElement
from utils.logger import Logger


class MultiWebElement:
    DEFAULT_TIMEOUT = 10

    def __init__(
        self,
        browser,
        formattable_xpath: str,
        description: str = None,
        timeout: int = None,
    ) -> None:
        self.index = 1
        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIMEOUT
        self.description = description if description else self.formattable_xpath.format("'i'")

    def __iter__(self) -> Self:
        self.index = 1
        return self

    def __next__(self) -> WebElement:
        try:
            current_element = WebElement(
                self.browser,
                self.formattable_xpath.format(self.index),
                f"{self.description}{self.index}",
            )
        except Exception as e:
            Logger.error(f"Ошибка при создании элемента {self.index}: {e}")
            raise StopIteration

        if not current_element.is_exists(timeout=1):
            raise StopIteration
        else:
            self.index += 1
            return current_element

    def __str__(self) -> str:
        return f"{self.__class__.__name__}{self.description}"

    def __repr__(self) -> str:
        return str(self)
