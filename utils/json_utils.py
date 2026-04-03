import json


class JsonUtils:
    @staticmethod
    def is_json(obj: str) -> bool:
        try:
            json.loads(obj)
            return True
        except ValueError:
            return False
