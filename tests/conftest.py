import os
import pytest
from faker import Faker
from utils.api_utils import ApiUtils
from services.university.university_service import UniversityService
from services.auth.auth_service import AuthService
from services.auth.models.register_request import RegisterRequest
from services.auth.models.login_request import LoginRequest


faker = Faker()

AUTH_URL = os.getenv("AUTH_SERVICE_URL", "http://localhost:8000")
UNIVERSITY_URL = os.getenv("UNIVERSITY_SERVICE_URL", "http://localhost:8001")


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

    register_response = auth_service.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email()
        )
    )
    assert register_response.detail == "User registered"

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
