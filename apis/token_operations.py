import requests
import os
import json

auth_endpoint = "http://localhost:8080/api/auth/token"
api_token_file = "api_token.json"

class TokenOperations():
    def __init__(self):
        self.password = os.getenv("PASSWORD")
        self.username = os.getenv("USER_NAME")
        self.token = self.get_token_from_json()  

    def get_token(self, endpoint: str):
        if os.path.exists(api_token_file):
            return self.get_token_from_json()  
        else:
            if self.is_token_valid(endpoint=endpoint):
                return self.token
            else:
                self.set_token()
                return self.token

      
    def set_token(self):
        response = requests.get(auth_endpoint, auth=(self.username, self.password))
        
        if response.status_code == 200:
            token = response.text.strip()
            if token:
                if os.path.exists(api_token_file):
                    with open(api_token_file, "a") as token_file:  
                        token_file.write(json.dumps({"token": token}) + "\n")  
                    

                else:
                    with open(api_token_file, "w") as token_file:  
                        token_file.write(json.dumps({"token": token}))  
                        

        elif response.status_code == 401:
            print("Invalid credentials")
            
        else:
            print(f"Failed to obtain token. Status code: {response.status_code}")
    
    def is_token_valid(self, endpoint: str):
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        protected_endpoint = endpoint
        response = requests.get(protected_endpoint, headers=headers)
        if(response.status_code == 401):
            return False
        elif(response.status_code == 200):
            return True
        
    def get_token_from_json(self):
        try:
            if os.path.exists(api_token_file):
                with open(api_token_file, "r") as json_file:
                    data = json.load(json_file)
                    token_value = data.get("token")
                    return token_value
            else:
                self.set_token()
                return self.get_token_from_json()
        except json.JSONDecodeError:
            self.set_token()
            return self.get_token_from_json()
    
    def get_response(self, endpoint: str):
        token = self.get_token(endpoint)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        protected_endpoint = endpoint
        response = requests.get(protected_endpoint, headers=headers)
        return response.json()
    
    



