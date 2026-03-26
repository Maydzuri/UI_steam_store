from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser.browser import Browser
from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from utils.logger import Logger


class UploadDragDropPage(BasePage):

    DROP_ZONE = "//div[@id='drag-drop-upload']"
    FILE_INPUT = "file-upload"
    FILE_NAME = "//div[contains(@class, 'dz-filename')]//span"
    CHECKMARK = "//div[contains(@class, 'dz-success-mark')]"
    PAGE_TITLE = "//h3[text()='File Uploader']"

    def __init__(self, browser: Browser):
        self.drop_zone = WebElement(browser, self.DROP_ZONE, description="Область для загрузки")
        self.file_input = Input(browser, self.FILE_INPUT, description="Скрытое поле выбора файла")
        self.file_name_label = Label(browser, self.FILE_NAME, description="Имя загруженного файла")
        self.checkmark = WebElement(browser, self.CHECKMARK, description="Галочка успеха")
        title_element = Label(browser, self.PAGE_TITLE, description="Заголовок страницы")
        super().__init__(browser, unique_element=title_element, name="UploadDragDropPage")

    def upload_via_drag_and_drop(self, file_path: str):
        Logger.info(f"Эмуляция drag-and-drop: {file_path}")

        self.file_input.send_keys(file_path, clear_first=False)

        self.browser.driver.execute_script("""
            var dropZone = arguments[0];
            var fileInput = arguments[1];
            var file = fileInput.files[0];

            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);

            var event = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });

            dropZone.dispatchEvent(event);
        """, self.drop_zone.wait_for_presence(), self.file_input.wait_for_presence())

    def get_uploaded_file_name(self, timeout: int = None) -> str:
        timeout = timeout or self.browser.DEFAULT_TIMEOUT
        element = WebDriverWait(self.browser.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, self.FILE_NAME))
        )
        WebDriverWait(self.browser.driver, timeout).until(
            lambda d: element.text.strip() != ""
        )
        return element.text.strip()

    def is_checkmark_displayed(self, timeout: int = None) -> bool:
        try:
            self.checkmark.wait_for_visible(timeout)
            return True
        except TimeoutException:
            return False
