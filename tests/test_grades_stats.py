from services.university.models.student_request import StudentRequest
from services.university.models.group_request import GroupRequest
from services.university.models.grade_request import GradeRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.models.subject_enum import SubjectEnum
from services.university.models.degree_enum import DegreeEnum
import random
from faker import Faker

faker = Faker()


class TestGradesStats:

    def _create_test_group(self, university_service_admin) -> int:
        group_request = GroupRequest(name=faker.name())
        group_response = university_service_admin.create_group(group_request)
        return group_response.id

    def _create_test_student(self, university_service_admin, group_id: int) -> int:
        student_request = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=DegreeEnum.BACHELOR,
            phone=faker.numerify("+7##########"),
            group_id=group_id
        )
        student_response = university_service_admin.create_student(student_request)
        return student_response.id

    def _create_test_teacher(self, university_service_admin) -> int:
        teacher_request = TeacherRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            subject=random.choice(list(SubjectEnum))
        )
        teacher_response = university_service_admin.create_teacher(teacher_request)
        return teacher_response.id

    def _create_test_grade(self, university_service_admin, student_id: int, teacher_id: int, grade: int) -> int:
        grade_request = GradeRequest(
            teacher_id=teacher_id,
            student_id=student_id,
            grade=grade
        )
        grade_response = university_service_admin.create_grade(grade_request)
        return grade_response.id

    def test_stats_returns_200_without_params(self, university_api_utils_admin):
        response = university_api_utils_admin.get("/grades/stats/")
        assert response.status_code == 200, \
            f"Ожидался статус 200, получен {response.status_code}"

    def test_stats_returns_200_with_student_id(self, university_api_utils_admin):
        response = university_api_utils_admin.get("/grades/stats/", params={"student_id": 1})
        assert response.status_code == 200, \
            f"Ожидался статус 200, получен {response.status_code}"

    def test_stats_returns_200_with_teacher_id(self, university_api_utils_admin):
        response = university_api_utils_admin.get("/grades/stats/", params={"teacher_id": 1})
        assert response.status_code == 200, \
            f"Ожидался статус 200, получен {response.status_code}"

    def test_stats_returns_200_with_group_id(self, university_api_utils_admin):
        response = university_api_utils_admin.get("/grades/stats/", params={"group_id": 1})
        assert response.status_code == 200, \
            f"Ожидался статус 200, получен {response.status_code}"

    def test_stats_returns_403_without_token(self, university_api_utils_anonym):
        response = university_api_utils_anonym.get("/grades/stats/")
        assert response.status_code == 403, \
            f"Ожидался статус 403, получен {response.status_code}"

    def test_stats_count_when_no_data(self, university_service_admin):
        group_id = self._create_test_group(university_service_admin)
        student_id = self._create_test_student(university_service_admin, group_id)

        stats = university_service_admin.get_grades_stats(student_id=student_id)

        assert stats.count == 0, \
            f"Ожидался count = 0, получен {stats.count}"
        assert stats.min is None, \
            f"Ожидался min = None, получен {stats.min}"
        assert stats.max is None, \
            f"Ожидался max = None, получен {stats.max}"
        assert stats.avg is None, \
            f"Ожидался avg = None, получен {stats.avg}"

    def test_stats_count_increases_after_grade_created(self, university_service_admin):
        group_id = self._create_test_group(university_service_admin)
        student_id = self._create_test_student(university_service_admin, group_id)
        teacher_id = self._create_test_teacher(university_service_admin)

        stats_before = university_service_admin.get_grades_stats(student_id=student_id)
        count_before = stats_before.count

        self._create_test_grade(university_service_admin, student_id, teacher_id, 4)

        stats_after = university_service_admin.get_grades_stats(student_id=student_id)
        count_after = stats_after.count

        assert count_after == count_before + 1, \
            f"Ожидался count = {count_before + 1}, получен {count_after}"

    def test_stats_min_calculated_correctly(self, university_service_admin):
        group_id = self._create_test_group(university_service_admin)
        student_id = self._create_test_student(university_service_admin, group_id)
        teacher_id = self._create_test_teacher(university_service_admin)

        self._create_test_grade(university_service_admin, student_id, teacher_id, 2)
        self._create_test_grade(university_service_admin, student_id, teacher_id, 5)

        stats = university_service_admin.get_grades_stats(student_id=student_id)
        assert stats.min == 2, \
            f"Ожидался min = 2, получен {stats.min}"
        assert stats.max == 5, \
            f"Ожидался max = 5, получен {stats.max}"
        assert stats.avg == 3.5, \
            f"Ожидался avg = 3.5, получен {stats.avg}"

    def test_stats_min_avg_max_logic(self, university_service_admin):
        group_id = self._create_test_group(university_service_admin)
        student_id = self._create_test_student(university_service_admin, group_id)
        teacher_id = self._create_test_teacher(university_service_admin)

        self._create_test_grade(university_service_admin, student_id, teacher_id, 3)
        self._create_test_grade(university_service_admin, student_id, teacher_id, 4)
        self._create_test_grade(university_service_admin, student_id, teacher_id, 5)

        stats = university_service_admin.get_grades_stats(student_id=student_id)
        assert stats.min <= stats.avg <= stats.max, \
            f"Некорректная статистика: min={stats.min}, avg={stats.avg}, max={stats.max}"

    def test_stats_consistency(self, university_service_admin):
        stats1 = university_service_admin.get_grades_stats()
        stats2 = university_service_admin.get_grades_stats()
        assert stats1.count == stats2.count, \
            f"count не совпадает: {stats1.count} != {stats2.count}"
        assert stats1.min == stats2.min, \
            f"min не совпадает: {stats1.min} != {stats2.min}"
        assert stats1.max == stats2.max, \
            f"max не совпадает: {stats1.max} != {stats2.max}"
        assert stats1.avg == stats2.avg, \
            f"avg не совпадает: {stats1.avg} != {stats2.avg}"
