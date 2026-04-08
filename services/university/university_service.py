from utils.api_utils import ApiUtils
from services.university.helpers.grades_helper import GradesHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.grade_request import GradeRequest
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest


class UniversityService:
    SERVICE_URL = "http://127.0.0.1:8889"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils
        self.grades_helper = GradesHelper(self.api_utils)
        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)

    def get_grades_stats(self, student_id: int = None, teacher_id: int = None, group_id: int = None):
        response = self.grades_helper.get_stats(student_id, teacher_id, group_id)
        return response.json()

    def create_grade(self, grade_request: GradeRequest):
        response = self.grades_helper.post_grade(data=grade_request.model_dump())
        return response.json()

    def create_group(self, group_request: GroupRequest):
        response = self.group_helper.post_group(json=group_request.model_dump())
        return response.json()

    def create_student(self, student_request: StudentRequest):
        response = self.student_helper.post_student(json=student_request.model_dump())
        return response.json()

    def get_students(self):
        response = self.student_helper.get_students()
        return response.json()

    def create_teacher(self, teacher_request: TeacherRequest):
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return response.json()
