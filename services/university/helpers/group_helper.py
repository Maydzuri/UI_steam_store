import requests
from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = "/groups"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_group(self, json: dict) -> requests.Response:
        return self.api_utils.post(self.ROOT_ENDPOINT, json=json)

    def get_groups(self) -> requests.Response:
        return self.api_utils.get(self.ROOT_ENDPOINT)

    def get_group(self, group_id: int) -> requests.Response:
        return self.api_utils.get(f"{self.ROOT_ENDPOINT}{group_id}/")
