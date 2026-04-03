from utils.api_utils import ApiUtils
from services.university.helpers.grades_helper import GradesHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.models.grades_stats_response import GradesStatsResponse


class UniversityService:
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils
        self.grades_helper = GradesHelper(self.api_utils)
        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)

    def get_grades_stats(self, student_id: int = None, teacher_id: int = None, group_id: int = None) -> GradesStatsResponse:
        response = self.grades_helper.get_stats(student_id, teacher_id, group_id)
        response.raise_for_status()
        return GradesStatsResponse(**response.json())

    def create_group(self, name: str) -> dict:
        response = self.group_helper.post_group(json={"name": name})
        response.raise_for_status()
        return response.json()

    def create_student(self, student_data: dict) -> dict:
        response = self.student_helper.post_student(json=student_data)
        response.raise_for_status()
        return response.json()
