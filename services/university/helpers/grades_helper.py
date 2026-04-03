import requests
from services.general.helpers.base_helper import BaseHelper


class GradesHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"
    STATS_ENDPOINT = f"{ENDPOINT_PREFIX}/stats/"

    def get_stats(self, student_id: int = None, teacher_id: int = None, group_id: int = None) -> requests.Response:
        params = {}
        if student_id is not None:
            params["student_id"] = student_id
        if teacher_id is not None:
            params["teacher_id"] = teacher_id
        if group_id is not None:
            params["group_id"] = group_id
        return self.api_utils.get(self.STATS_ENDPOINT, params=params)
