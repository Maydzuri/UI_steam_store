import os


class TestUploadDragDrop:

    def test_upload_via_drag_and_drop(self, upload_page):
        page = upload_page

        file_name = "test_file.txt"
        file_path = os.path.abspath(f"resources/{file_name}")

        page.upload_via_drag_and_drop(file_path)

        uploaded_name = page.get_uploaded_file_name()
        assert uploaded_name == file_name, \
            f"Ожидалось имя файла '{file_name}', получено '{uploaded_name}'"

        assert page.is_checkmark_displayed(), \
            "Галочка успеха не появилась"
