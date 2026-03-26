from selenium.common.exceptions import TimeoutException
from browser.browser import Browser
from pages.base_page import BasePage
from elements.input import Input
from elements.button import Button
from elements.label import Label
from utils.logger import Logger


class UploadPage(BasePage):

    FILE_INPUT = "file-upload"
    UPLOAD_BUTTON = "file-submit"
    SUCCESS_MESSAGE = "//h3[text()='File Uploaded!']"
    UPLOADED_FILE = "uploaded-files"
    PAGE_TITLE = "//h3[text()='File Uploader']"

    def __init__(self, browser: Browser):
        self.file_input = Input(browser, self.FILE_INPUT, description="Поле выбора файла")
        self.upload_button = Button(browser, self.UPLOAD_BUTTON, description="Кнопка Upload")
        self.success_label = Label(browser, self.SUCCESS_MESSAGE, description="Сообщение об успехе")
        self.uploaded_file_label = Label(browser, self.UPLOADED_FILE, description="Имя загруженного файла")
        title_element = Label(browser, self.PAGE_TITLE, description="Заголовок страницы")
        super().__init__(browser, unique_element=title_element, name="UploadPage")

    def upload_file(self, file_path: str):
        Logger.info(f"Загрузка файла: {file_path}")
        self.file_input.send_keys(file_path, clear_first=False)
        self.upload_button.click()

    def is_success_message_displayed(self, timeout: int = None) -> bool:
        try:
            self.success_label.wait_for_visible(timeout)
            return True
        except TimeoutException:
            return False

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_file_label.get_text()
