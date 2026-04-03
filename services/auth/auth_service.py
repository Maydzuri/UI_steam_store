from utils.api_utils import ApiUtils
from services.auth.helpers.authorization_helper import AuthorizationHelper
from services.auth.helpers.user_helper import UserHelper
from services.auth.models.login_request import LoginRequest
from services.auth.models.login_response import LoginResponse
from services.auth.models.register_request import RegisterRequest
from services.auth.models.success_response import SuccessResponse


class AuthService:
    SERVICE_URL = "http://127.0.0.1:8000"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils
        self.authorization_helper = AuthorizationHelper(self.api_utils)
        self.user_helper = UserHelper(self.api_utils)

    def register_user(self, register_request: RegisterRequest) -> SuccessResponse:
        response = self.authorization_helper.post_register(data=register_request.model_dump())
        response.raise_for_status()
        return SuccessResponse(**response.json())

    def login_user(self, login_request: LoginRequest) -> LoginResponse:
        response = self.authorization_helper.post_login(data=login_request.model_dump())
        response.raise_for_status()
        return LoginResponse(**response.json())

    def get_current_user(self) -> dict:
        response = self.user_helper.get_me()
        response.raise_for_status()
        return response.json()
