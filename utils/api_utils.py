import json
import requests
from requests import Session

from utils.logger import Logger
from utils.json_utils import JsonUtils


def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        try:
            response = func(*args, **kwargs)
            Logger.info(f"Response status code='{response.status_code}', elapsed_time='{response.elapsed}'")

            if JsonUtils.is_json(response.text):
                body = json.dumps(response.json(), indent=2, ensure_ascii=False)
                Logger.debug(f"Response body: {body}")
            else:
                Logger.debug(f"Response body (non-JSON): {response.text[:500]}")

            return response
        except Exception as e:
            Logger.error(f"Request failed: {e}")
            raise

    return _log_response


class ApiUtils:
    def __init__(self, url: str, headers: dict = None):
        if headers is None:
            headers = {}
        self.session = Session()
        self.session.headers.update(headers)
        self.url = url

    @log_response
    def get(self, endpoint_url: str, **kwargs) -> requests.Response:
        return self.session.get(self.url + endpoint_url, **kwargs)

    @log_response
    def post(self, endpoint_url: str, data=None, json=None, **kwargs) -> requests.Response:
        return self.session.post(self.url + endpoint_url, data=data, json=json, **kwargs)

    @log_response
    def put(self, endpoint_url: str, **kwargs) -> requests.Response:
        return self.session.put(self.url + endpoint_url, **kwargs)

    @log_response
    def delete(self, endpoint_url: str, **kwargs) -> requests.Response:
        return self.session.delete(self.url + endpoint_url, **kwargs)
