import os
from utils.logger import Logger


class TestUploadDialog:

    def test_upload_via_drop_zone(self, upload_dialog_page):
        page = upload_dialog_page

        file_name = "test_file.txt"
        file_path = os.path.abspath(f"resources/{file_name}")

        Logger.info(f"Путь к файлу: {file_path}")

        page.upload_file_via_dialog(file_path)

        uploaded_name = page.get_uploaded_file_name()
        assert uploaded_name == file_name, \
            f"Ожидалось имя файла '{file_name}', получено '{uploaded_name}'"

        assert page.is_checkmark_displayed(), \
            "Галочка успеха не появилась"
