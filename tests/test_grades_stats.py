from services.university.models.student_request import StudentRequest
from services.university.models.group_request import GroupRequest
from services.university.models.grade_request import GradeRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.models.subject_enum import SubjectEnum
from services.university.models.degree_enum import DegreeEnum
from config.settings import MIN_GRADE, MAX_GRADE
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

    def test_stats_returns_200_without_params(self, university_service_admin):
        stats = university_service_admin.get_grades_stats()
        assert stats.count >= 0

    def test_stats_returns_200_with_student_id(self, university_service_admin):
        stats = university_service_admin.get_grades_stats(student_id=1)
        assert stats.count >= 0

    def test_stats_returns_200_with_teacher_id(self, university_service_admin):
        stats = university_service_admin.get_grades_stats(teacher_id=1)
        assert stats.count >= 0

    def test_stats_returns_200_with_group_id(self, university_service_admin):
        stats = university_service_admin.get_grades_stats(group_id=1)
        assert stats.count >= 0

    def test_stats_returns_403_without_token(self, university_api_utils_anonym):
        response = university_api_utils_anonym.get("/grades/stats/")
        assert response.status_code == 403, \
            f"Ожидался статус 403, получен {response.status_code}"

    def test_stats_count_when_no_data(self, university_service_admin, student_without_grades):
        stats = university_service_admin.get_grades_stats(student_id=student_without_grades)
        assert stats.count == 0, \
            f"Ожидался count = 0, получен {stats.count}"

    def test_stats_min_is_none_when_no_data(self, university_service_admin, student_without_grades):
        stats = university_service_admin.get_grades_stats(student_id=student_without_grades)
        assert stats.min is None, \
            f"Ожидался min = None, получен {stats.min}"

    def test_stats_max_is_none_when_no_data(self, university_service_admin, student_without_grades):
        stats = university_service_admin.get_grades_stats(student_id=student_without_grades)
        assert stats.max is None, \
            f"Ожидался max = None, получен {stats.max}"

    def test_stats_avg_is_none_when_no_data(self, university_service_admin, student_without_grades):
        stats = university_service_admin.get_grades_stats(student_id=student_without_grades)
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

    def test_stats_min_avg_max_logic(self, university_service_admin):
        group_id = self._create_test_group(university_service_admin)
        student_id = self._create_test_student(university_service_admin, group_id)
        teacher_id = self._create_test_teacher(university_service_admin)

        grades = [random.randint(MIN_GRADE, MAX_GRADE) for _ in range(3)]
        for grade in grades:
            self._create_test_grade(university_service_admin, student_id, teacher_id, grade)

        stats = university_service_admin.get_grades_stats(student_id=student_id)
        assert stats.min <= stats.avg <= stats.max, \
            f"Некорректная статистика: min={stats.min}, avg={stats.avg}, max={stats.max}"

    def test_stats_consistency(self, university_service_admin):
        stats1 = university_service_admin.get_grades_stats()
        stats2 = university_service_admin.get_grades_stats()

        assert stats1 == stats2, \
            f"Статистика не совпадает после повторного запроса:\n{stats1}\n{stats2}"
