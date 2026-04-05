from services.general.helpers.base_helper import BaseHelper


class UserHelper(BaseHelper):
    ENDPOINT_PREFIX = "/users"
    ME_ENDPOINT = f"{ENDPOINT_PREFIX}/me/"

    def get_me(self) -> dict:
        response = self.api_utils.get(self.ME_ENDPOINT)
        response.raise_for_status()
        return response.json()
