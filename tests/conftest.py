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
from services.university.models.degree_enum import DegreeEnum
from services.university.models.subject_enum import SubjectEnum
from services.university.models.grade_request import GradeRequest


faker = Faker()

AUTH_URL = os.getenv("AUTH_SERVICE_URL", "http://localhost:8888")
UNIVERSITY_URL = os.getenv("UNIVERSITY_SERVICE_URL", "http://localhost:8889")


@pytest.fixture(scope="session", autouse=True)
def auth_service_readiness():
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AuthService.SERVICE_URL + "/docs")
            response.raise_for_status()
            break
        except:
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
        except:
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
def test_group(university_service_admin):
    group_request = GroupRequest(name=faker.name())
    group_response = university_service_admin.create_group(group_request)
    return group_response.id

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
    student_response = university_service_admin.create_student(student_request)
    return student_response.id

@pytest.fixture(scope="function")
def test_teacher(university_service_admin):
    teacher_request = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice(list(SubjectEnum))
    )
    teacher_response = university_service_admin.create_teacher(teacher_request)
    return teacher_response.id

@pytest.fixture(scope="function")
def student_with_grades(university_service_admin, test_student, test_teacher):
    grade_request_1 = GradeRequest(
        teacher_id=test_teacher,
        student_id=test_student,
        grade=4
    )
    grade_request_2 = GradeRequest(
        teacher_id=test_teacher,
        student_id=test_student,
        grade=5
    )
    university_service_admin.create_grade(grade_request_1)
    university_service_admin.create_grade(grade_request_2)
    return test_student
