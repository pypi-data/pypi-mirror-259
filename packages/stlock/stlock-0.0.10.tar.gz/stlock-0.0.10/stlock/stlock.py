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
        self.__url_prefix = '/api/v0/users'

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
        response = requests.post(
            self.__endpoint + self.__url_prefix + "/login", data=json.dumps(data), headers=headers
        )
        return response.json(), response.status_code

    def do_refresh(self, refresh_token):
        headers = {
            "x-api-key": self.__api_key,
            "Authorization": f"bearer {refresh_token}"
        }
        response = requests.get(
            self.__endpoint + self.__url_prefix + "/refresh", headers=headers
        )
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
        response = requests.post(
            self.__endpoint + self.__url_prefix + "/register", data=json.dumps(data), headers=headers
        )
        return response.json(), response.status_code

    def unauthorized(self, refresh_token):
        headers = {
            "x-api-key": self.__api_key,
            "Authorization": f"bearer {refresh_token}"
        }
        response = requests.post(
            self.__endpoint + self.__url_prefix + "/logout", headers=headers
        )
        return response.json(), response.status_code

    def decode(self, token):
        data = jwt.decode(token, algorithms=["HS256"], verify=self.__api_key)
        return data

    def policy(self, func):
        def wrapper():
            print("Checking policy", self.__endpoint)
            func()

        return wrapper

    def check_grant(self, access_token: str, method: str = 'get', path: str = ''):
        headers = {
            "x-api-key": self.__api_key,
            "Authorization": f"bearer {access_token}"
        }
        data = {
            "method": method,
            "path": path
        }
        response = requests.post(
            self.__endpoint + self.__url_prefix + "/grant", data=json.dumps(data), headers=headers
        )
        return response.json(), response.status_code

    def update_username(self, access_token: str, new_username):
        headers = {
            "x-api-key": self.__api_key,
            "Authorization": f"bearer {access_token}"
        }
        data = {
            "user_pool_id": self.__user_pool_id,
            "username": new_username
        }
        response = requests.patch(
            self.__endpoint + self.__url_prefix + "/username", data=json.dumps(data), headers=headers
        )
        return response.json(), response.status_code

    def update_email(self, access_token: str, new_email):
        headers = {
            "x-api-key": self.__api_key,
            "Authorization": f"bearer {access_token}"
        }
        data = {
            "user_pool_id": self.__user_pool_id,
            "email": new_email
        }
        response = requests.patch(
            self.__endpoint + self.__url_prefix + "/email", data=json.dumps(data), headers=headers
        )
        return response.json(), response.status_code

    def update_password(self, access_token: str, old_password: str, new_password: str):
        headers = {
            "x-api-key": self.__api_key,
            "Authorization": f"bearer {access_token}"
        }
        data = {
            "old_password": old_password,
            "new_password": new_password
        }
        response = requests.patch(
            self.__endpoint + self.__url_prefix + "/password", data=json.dumps(data), headers=headers
        )
        return response.json(), response.status_code
