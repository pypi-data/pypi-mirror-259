import json

import requests
import jwt


# Main class
class AuthClient:
    def __init__(self, endpoint, user_pool_id, owner_id, api_key):
        self.__endpoint = endpoint.removesuffix("/")
        self.__user_pool_id = user_pool_id
        self.__owner_id = owner_id
        self.__api_key = api_key

    def authorize_user(self, username, password):
        headers = {
            "x-api-key": self.__api_key
        }
        data = {
            "user_pool_id": self.__user_pool_id,
            "owner_id": self.__owner_id,
            "username": username,
            "password": password,
        }
        response = requests.post(self.__endpoint + "/api/v0/users/login", data=json.dumps(data), headers=headers)
        return response.json(), response.status_code

    def do_refresh(self, refresh_token):
        headers = {
            "x-api-key": self.__api_key,
            "Authorization": f"bearer {refresh_token}"
        }
        response = requests.get(self.__endpoint + "/api/v0/users/refresh", headers=headers)
        return response.json(), response.status_code

    def register(self, username, email, phone, password):
        headers = {
            "x-api-key": self.__api_key
        }
        data = {
            "user_pool_id": self.__user_pool_id,
            "owner_id": self.__owner_id,
            "username": username,
            "email": email,
            "phone": phone,
            "password": password,
        }
        response = requests.post(self.__endpoint + "/api/v0/users/register", data=json.dumps(data), headers=headers)
        return response.json(), response.status_code

    def unauthorized(self, refresh_token):
        headers = {
            "x-api-key": self.__api_key,
            "Authorization": f"bearer {refresh_token}"
        }
        response = requests.post(self.__endpoint + "/api/v0/users/logout", headers=headers)
        return response.json(), response.status_code

    def decode(self, token):
        data = jwt.decode(token, algorithms=["HS256"], verify=self.__api_key)
        return data

    def policy(self, func):
        def wrapper():
            print("Checking policy", self.__endpoint)
            func()

        return wrapper




