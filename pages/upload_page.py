import time
from browser.browser import Browser
from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from utils.logger import Logger
from utils.pyautogui_utils import PyAutoGUIUtilities


class UploadPage(BasePage):

    DROP_ZONE = "//*[@id='drag-drop-upload']"
    FILE_INPUT = "file-upload"
    FILE_NAME = "//div[contains(@class, 'dz-filename')]//span"
    CHECKMARK = "//div[contains(@class, 'dz-success-mark')]"
    UPLOAD_BUTTON = "file-submit"
    SUCCESS_MESSAGE = "//h3[text()='File Uploaded!']"
    PAGE_TITLE = "//h3[text()='File Uploader']"

    def __init__(self, browser: Browser):
        self.drop_zone = WebElement(browser, self.DROP_ZONE, description="Область для загрузки")
        self.file_input = Input(browser, self.FILE_INPUT, description="Поле выбора файла")
        self.file_name_label = WebElement(browser, self.FILE_NAME, description="Имя загруженного файла")
        self.checkmark = WebElement(browser, self.CHECKMARK, description="Галочка успеха")
        self.upload_button = WebElement(browser, self.UPLOAD_BUTTON, description="Кнопка Upload")
        self.success_label = Label(browser, self.SUCCESS_MESSAGE, description="Сообщение об успехе")
        title_element = Label(browser, self.PAGE_TITLE, description="Заголовок страницы")
        super().__init__(browser, unique_element=title_element, name="UploadPage")

    def upload_via_input(self, file_path: str):
        Logger.info(f"Загрузка через input: {file_path}")
        self.file_input.send_keys(file_path, clear_first=False)
        self.upload_button.click()

    def is_success_message_displayed(self) -> bool:
        return self.success_label.is_exists()

    def upload_via_dialog(self, file_path: str):
        Logger.info(f"Загрузка через диалог: {file_path}")
        self.drop_zone.click()
        time.sleep(1)
        PyAutoGUIUtilities.upload_file(file_path)

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

    def get_uploaded_file_name(self) -> str:
        return self.file_name_label.get_text()

    def is_checkmark_displayed(self) -> bool:
        return self.checkmark.is_exists()
