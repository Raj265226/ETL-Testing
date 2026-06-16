import requests
from config.settings import BASE_URL

class APIClient:

    def get_users(self):

        response = requests.get(
            f"{BASE_URL}/users"
        )

        return response

    def create_user(self, payload):

        response = requests.post(
            f"{BASE_URL}/users",
            json=payload
        )

        return response