import requests
from src.apis.auth.token_operations import TokenOperations


class FetchMethods:
    def __init__(self):
        self.token_operation = TokenOperations()

    def get_request(self, endpoint: str):
        token = self.token_operation.get_token(endpoint)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            return response.status_code

    def get_request_with_body(self, endpoint: str, date):
        date_dict = {
            "date": date
        }
        token = self.token_operation.get_token(endpoint)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.get(endpoint, headers=headers, json=date_dict)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code} at request_with_body: {response}")
            return response.status_code

    def post_request(self, endpoint: str, data: dict):
        token = self.token_operation.get_token(endpoint)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.post(endpoint, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            return response.status_code
