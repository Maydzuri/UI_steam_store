import os


class TestUploadSimple:

    def test_upload_via_input(self, upload_page):
        page = upload_page

        file_name = "test_file.txt"
        file_path = os.path.abspath(f"resources/{file_name}")

        page.upload_via_input(file_path)

        assert page.is_success_message_displayed(), \
            "Сообщение 'File Uploaded!' не появилось"

        uploaded_name = page.get_uploaded_file_name()
        assert uploaded_name == file_name, \
            f"Ожидалось имя файла '{file_name}', получено '{uploaded_name}'"
