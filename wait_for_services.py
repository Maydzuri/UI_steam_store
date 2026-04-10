import time
import sys
import os
import requests

AUTH_URL = os.getenv("AUTH_SERVICE_API_URL", "http://auth:8000")
UNIVERSITY_URL = os.getenv("UNIVERSITY_SERVICE_API_URL", "http://university:8000")

SERVICES = [
    {
        "url": f"{AUTH_URL}/docs",
        "name": "Auth Service"
    },
    {
        "url": f"{UNIVERSITY_URL}/docs",
        "name": "University Service"
    }
]

TIMEOUT = 180
RETRY_INTERVAL = 2


def wait_for_services() -> None:
    start_time = time.time()

    for service in SERVICES:
        url = service["url"]
        name = service["name"]

        print(f"Waiting for {name} at {url}...")

        while time.time() < start_time + TIMEOUT:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"{name} is ready!")
                    break
            except requests.exceptions.RequestException:
                pass

            time.sleep(RETRY_INTERVAL)
        else:
            print(f"{name} failed to start within {TIMEOUT} seconds")
            sys.exit(1)

    print("All services are ready!")


if __name__ == "__main__":
    wait_for_services()
