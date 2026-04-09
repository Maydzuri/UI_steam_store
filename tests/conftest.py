import os
import time
import random
import pytest
import requests
from faker import Faker
from utils.api_utils import ApiUtils
from services.university.university_service import UniversityService
from services.auth.auth_service import AuthService
from services.auth.models.register_request import RegisterRequest
from services.auth.models.login_request import LoginRequest
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.models.grade_request import GradeRequest
from services.university.models.degree_enum import DegreeEnum
from services.university.models.subject_enum import SubjectEnum

faker = Faker()

AUTH_URL = os.getenv("AUTH_SERVICE_API_URL", "http://localhost:8888")
UNIVERSITY_URL = os.getenv("UNIVERSITY_SERVICE_API_URL", "http://localhost:8889")


@pytest.fixture(scope="session", autouse=True)
def auth_service_readiness():
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AUTH_URL + "/docs")
            response.raise_for_status()
            break
        except Exception:
            time.sleep(1)
    else:
        raise RuntimeError(f"Auth service wasn't started during '{timeout}' seconds.")

@pytest.fixture(scope="session", autouse=True)
def university_service_readiness():
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(UNIVERSITY_URL + "/docs")
            response.raise_for_status()
            break
        except Exception:
            time.sleep(1)
    else:
        raise RuntimeError(f"University service wasn't started during '{timeout}' seconds.")

@pytest.fixture(scope="function")
def auth_api_utils_anonym():
    return ApiUtils(url=AUTH_URL)

@pytest.fixture(scope="function")
def university_api_utils_anonym():
    return ApiUtils(url=UNIVERSITY_URL)

@pytest.fixture(scope="function")
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

    auth_service.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email()
        )
    )

    login_response = auth_service.login_user(
        login_request=LoginRequest(username=username, password=password)
    )
    return login_response.access_token


@pytest.fixture(scope="function")
def auth_api_utils_admin(access_token):
    return ApiUtils(url=AUTH_URL, headers={"Authorization": f"Bearer {access_token}"})

@pytest.fixture(scope="function")
def university_api_utils_admin(access_token):
    return ApiUtils(url=UNIVERSITY_URL, headers={"Authorization": f"Bearer {access_token}"})

@pytest.fixture(scope="function")
def university_service_admin(university_api_utils_admin):
    return UniversityService(university_api_utils_admin)

@pytest.fixture(scope="function")
def university_service_anonym(university_api_utils_anonym):
    return UniversityService(university_api_utils_anonym)

@pytest.fixture(scope="function")
def test_student(university_service_admin, test_group):
    student_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=test_group
    )
    return university_service_admin.create_student(student_request).id

@pytest.fixture(scope="function")
def test_group(university_service_admin):
    group_request = GroupRequest(name=faker.name())
    return university_service_admin.create_group(group_request).id

@pytest.fixture(scope="function")
def test_teacher(university_service_admin):
    teacher_request = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice(list(SubjectEnum))
    )
    return university_service_admin.create_teacher(teacher_request).id

@pytest.fixture(scope="function")
def student_a_with_grades(university_service_admin, test_group, test_teacher):
    student_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=test_group
    )
    student = university_service_admin.create_student(student_request).id

    grade_request_1 = GradeRequest(teacher_id=test_teacher, student_id=student, grade=4)
    grade_request_2 = GradeRequest(teacher_id=test_teacher, student_id=student, grade=5)
    university_service_admin.create_grade(grade_request_1)
    university_service_admin.create_grade(grade_request_2)
    return student

@pytest.fixture(scope="function")
def student_b_with_grades(university_service_admin, test_group, test_teacher):
    student_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=test_group
    )
    student = university_service_admin.create_student(student_request).id

    grade_request_1 = GradeRequest(teacher_id=test_teacher, student_id=student, grade=2)
    grade_request_2 = GradeRequest(teacher_id=test_teacher, student_id=student, grade=3)
    grade_request_3 = GradeRequest(teacher_id=test_teacher, student_id=student, grade=3)
    university_service_admin.create_grade(grade_request_1)
    university_service_admin.create_grade(grade_request_2)
    university_service_admin.create_grade(grade_request_3)
    return student

@pytest.fixture(scope="function")
def teacher_x_with_grades(university_service_admin, test_group):
    teacher_request = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice(list(SubjectEnum))
    )
    teacher = university_service_admin.create_teacher(teacher_request).id

    student1_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=test_group
    )
    student1 = university_service_admin.create_student(student1_request).id

    student2_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=test_group
    )
    student2 = university_service_admin.create_student(student2_request).id

    grade_request_1 = GradeRequest(teacher_id=teacher, student_id=student1, grade=5)
    grade_request_2 = GradeRequest(teacher_id=teacher, student_id=student1, grade=4)
    grade_request_3 = GradeRequest(teacher_id=teacher, student_id=student2, grade=5)
    university_service_admin.create_grade(grade_request_1)
    university_service_admin.create_grade(grade_request_2)
    university_service_admin.create_grade(grade_request_3)
    return teacher

@pytest.fixture(scope="function")
def teacher_y_with_grades(university_service_admin, test_group):
    teacher_request = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice(list(SubjectEnum))
    )
    teacher = university_service_admin.create_teacher(teacher_request).id

    student_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=test_group
    )
    student = university_service_admin.create_student(student_request).id

    grade_request_1 = GradeRequest(teacher_id=teacher, student_id=student, grade=2)
    grade_request_2 = GradeRequest(teacher_id=teacher, student_id=student, grade=3)
    university_service_admin.create_grade(grade_request_1)
    university_service_admin.create_grade(grade_request_2)
    return teacher

@pytest.fixture(scope="function")
def group1_with_grades(university_service_admin, test_teacher):
    group_request = GroupRequest(name=faker.name())
    group = university_service_admin.create_group(group_request).id

    student_a_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=group
    )
    student_a = university_service_admin.create_student(student_a_request).id

    student_b_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=group
    )
    student_b = university_service_admin.create_student(student_b_request).id

    grade_request_1 = GradeRequest(teacher_id=test_teacher, student_id=student_a, grade=5)
    grade_request_2 = GradeRequest(teacher_id=test_teacher, student_id=student_a, grade=4)
    grade_request_3 = GradeRequest(teacher_id=test_teacher, student_id=student_b, grade=3)
    university_service_admin.create_grade(grade_request_1)
    university_service_admin.create_grade(grade_request_2)
    university_service_admin.create_grade(grade_request_3)
    return group

@pytest.fixture(scope="function")
def group2_with_grades(university_service_admin, test_teacher):
    group_request = GroupRequest(name=faker.name())
    group = university_service_admin.create_group(group_request).id

    student_c_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=group
    )
    student_c = university_service_admin.create_student(student_c_request).id

    grade_request_1 = GradeRequest(teacher_id=test_teacher, student_id=student_c, grade=5)
    grade_request_2 = GradeRequest(teacher_id=test_teacher, student_id=student_c, grade=5)
    university_service_admin.create_grade(grade_request_1)
    university_service_admin.create_grade(grade_request_2)
    return group

@pytest.fixture(scope="function")
def student_a_teacher_x_with_grade(university_service_admin, test_group):
    teacher_x_request = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice(list(SubjectEnum))
    )
    teacher_x = university_service_admin.create_teacher(teacher_x_request).id

    teacher_y_request = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice(list(SubjectEnum))
    )
    teacher_y = university_service_admin.create_teacher(teacher_y_request).id

    student_a_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=test_group
    )
    student_a = university_service_admin.create_student(student_a_request).id

    student_b_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=DegreeEnum.BACHELOR,
        phone=faker.numerify("+7##########"),
        group_id=test_group
    )
    student_b = university_service_admin.create_student(student_b_request).id

    grade_request_1 = GradeRequest(teacher_id=teacher_x, student_id=student_a, grade=5)
    grade_request_2 = GradeRequest(teacher_id=teacher_y, student_id=student_a, grade=4)
    grade_request_3 = GradeRequest(teacher_id=teacher_x, student_id=student_b, grade=3)
    university_service_admin.create_grade(grade_request_1)
    university_service_admin.create_grade(grade_request_2)
    university_service_admin.create_grade(grade_request_3)
    return student_a, teacher_x

@pytest.fixture(scope="function")
def max_student_id(university_service_admin):
    students = university_service_admin.get_students()
    if not students:
        return 0
    ids = [s.id for s in students]
    return max(ids)
