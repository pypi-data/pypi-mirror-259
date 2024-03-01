import json
import os
from unittest import mock

from stlock import AuthClient

import pytest


@pytest.fixture()
def auth_client():
    client = AuthClient(
        endpoint="ENDPOINT",
        api_key="API_KEY",
        owner_id="OWNER_ID",
        user_pool_id="USER_POOL_ID",
    )
    return client


@mock.patch("stlock.stlock.requests.post")
def test_register(mock_request, auth_client):
    json_response = {
        "policy_ids": [],
        "user_pool_id": "0e2173b5-b55f-4ea4-bec5-450e2c12a458",
        "owner_id": "b3893a06-5931-4160-9e62-938ab173b6c8",
        "username": "test",
        "email": "test@gmail.com",
        "phone": "79000000000",
        "id": "ee70dcc3-a79d-49b7-8d7e-54cac4cf054f",
        "status": "ACTIVE",
        "creation_timestamp": 1694104465
    }

    mock_data = mock.MagicMock()
    mock_data.status_code = 200
    mock_data.json.return_value = json_response
    user = {
        "username": "test",
        "email": "test@gmail.com",
        "phone": "79000000000",
        "password": "test"
    }

    mock_request.return_value = mock_data
    response = auth_client.register(**user)

    assert response[0] == json_response
    assert response[1] == 200


@mock.patch("stlock.stlock.requests.post")
def test_authorize(mock_request, auth_client):
    tokens = {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlZWQyNTdlMi1iNzUzLTQ5MjktOGNiZi02ZWVjOTg2ODM1YzQiLCJleHAiOjE2OTQxMDQ2MDcsImlhdCI6MTY5NDEwNDAwNywidHlwZSI6IkFDQ0VTUyIsImF1ZCI6IlVTRVIiLCJzdWIiOiJjZjdmZGZjNi1hNTRkLTQwMWUtYjFhNS0wYWJiYWQxY2M2NDMiLCJvd25lcl9zdWIiOiJiMzg5M2EwNi01OTMxLTQxNjAtOWU2Mi05MzhhYjE3M2I2YzgiLCJ1c2VyX3Bvb2xfc3ViIjoiMGUyMTczYjUtYjU1Zi00ZWE0LWJlYzUtNDUwZTJjMTJhNDU4In0.X7Qnpn6nBIqIkJX0s3F0wjXHqAEADx8i2VdNdBBDieU",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkZDVhNWI0Zi0yNWRkLTRhNGItOTNmZC1jMjBlZDJmYmI3ZGYiLCJleHAiOjE2OTQxMDc2MDcsImlhdCI6MTY5NDEwNDAwNywidHlwZSI6IlJFRlJFU0giLCJhdWQiOiJVU0VSIiwic3ViIjoiY2Y3ZmRmYzYtYTU0ZC00MDFlLWIxYTUtMGFiYmFkMWNjNjQzIiwib3duZXJfc3ViIjoiYjM4OTNhMDYtNTkzMS00MTYwLTllNjItOTM4YWIxNzNiNmM4IiwidXNlcl9wb29sX3N1YiI6IjBlMjE3M2I1LWI1NWYtNGVhNC1iZWM1LTQ1MGUyYzEyYTQ1OCJ9.j6DuBsXPhV67j-DfAFqI8KvFAoSgPIvA4qz5x1Tof5k"
    }
    mock_data = mock.MagicMock()
    mock_data.status_code = 200
    mock_data.json.return_value = tokens

    username = password = "test"

    mock_request.return_value = mock_data
    response = auth_client.authorize_user(username, password)

    assert response[0] == tokens
    assert response[1] == 200


@mock.patch("stlock.stlock.requests.get")
def test_refresh(mock_request, auth_client):
    tokens = {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlZWQyNTdlMi1iNzUzLTQ5MjktOGNiZi02ZWVjOTg2ODM1YzQiLCJleHAiOjE2OTQxMDQ2MDcsImlhdCI6MTY5NDEwNDAwNywidHlwZSI6IkFDQ0VTUyIsImF1ZCI6IlVTRVIiLCJzdWIiOiJjZjdmZGZjNi1hNTRkLTQwMWUtYjFhNS0wYWJiYWQxY2M2NDMiLCJvd25lcl9zdWIiOiJiMzg5M2EwNi01OTMxLTQxNjAtOWU2Mi05MzhhYjE3M2I2YzgiLCJ1c2VyX3Bvb2xfc3ViIjoiMGUyMTczYjUtYjU1Zi00ZWE0LWJlYzUtNDUwZTJjMTJhNDU4In0.X7Qnpn6nBIqIkJX0s3F0wjXHqAEADx8i2VdNdBBDieU",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkZDVhNWI0Zi0yNWRkLTRhNGItOTNmZC1jMjBlZDJmYmI3ZGYiLCJleHAiOjE2OTQxMDc2MDcsImlhdCI6MTY5NDEwNDAwNywidHlwZSI6IlJFRlJFU0giLCJhdWQiOiJVU0VSIiwic3ViIjoiY2Y3ZmRmYzYtYTU0ZC00MDFlLWIxYTUtMGFiYmFkMWNjNjQzIiwib3duZXJfc3ViIjoiYjM4OTNhMDYtNTkzMS00MTYwLTllNjItOTM4YWIxNzNiNmM4IiwidXNlcl9wb29sX3N1YiI6IjBlMjE3M2I1LWI1NWYtNGVhNC1iZWM1LTQ1MGUyYzEyYTQ1OCJ9.j6DuBsXPhV67j-DfAFqI8KvFAoSgPIvA4qz5x1Tof5k"
    }
    mock_data = mock.MagicMock()
    mock_data.status_code = 200
    mock_data.json.return_value = tokens

    refresh_token = "some_token"

    mock_request.return_value = mock_data
    response = auth_client.do_refresh(refresh_token)

    assert response[0] == tokens
    assert response[1] == 200


@mock.patch("stlock.stlock.requests.post")
def test_unauthorized(mock_request, auth_client):
    mock_data = mock.MagicMock()
    mock_data.status_code = 200
    mock_data.json.return_value = None

    refresh_token = "some_token"

    mock_request.return_value = mock_data
    response = auth_client.unauthorized(refresh_token)

    assert response[0] is None
    assert response[1] == 200
