from services.general.helpers.base_helper import BaseHelper


class GradesHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"
    STATS_ENDPOINT = f"{ENDPOINT_PREFIX}/stats/"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def get_stats(self, student_id: int = None, teacher_id: int = None, group_id: int = None) -> dict:
        params = {}
        if student_id is not None:
            params["student_id"] = student_id
        if teacher_id is not None:
            params["teacher_id"] = teacher_id
        if group_id is not None:
            params["group_id"] = group_id
        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        response.raise_for_status()
        return response.json()

    def post_grade(self, data: dict):
        return self.api_utils.post(self.ROOT_ENDPOINT, data=data)
