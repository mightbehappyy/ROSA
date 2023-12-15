import requests
from token_operations import TokenOperations

class FetchMethods:
    def __init__(self):
         self.token_operation = TokenOperations()

    def get_response(self, endpoint: str):
            token = self.token_operation.get_token(endpoint)
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            protected_endpoint = endpoint
            response = requests.get(protected_endpoint, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Request failed with status code: {response.status_code}")
                return None
    def post_response(self, endpoint: str, data: dict):
            token = self.token_operation.get_token(endpoint)
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            response = requests.post(endpoint, headers=headers, json=data)
            if response.status_code == 200:
                return response.json()
            else:
                print(response.json().get("message"))
                print(f"Request failed with status code: {response.status_code}")
                return None

# fetch_methods = FetchMethods()
# print(fetch_methods.get_response("http://localhost:8080/api/reserva-lab/eventos-da-semana"))
