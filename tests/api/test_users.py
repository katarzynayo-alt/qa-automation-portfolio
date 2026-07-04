"""API-тесты на reqres.in: CRUD по пользователям."""

import pytest
import requests

pytestmark = pytest.mark.api

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "free_user_3G2W1w37o2uxnMeFcAp198R3Dqk"}  # reqres.in требует этот заголовок


def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)

    assert response.status_code == 200
    body = response.json()
    assert body["page"] == 2
    assert len(body["data"]) > 0


def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2


def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/23", headers=HEADERS)

    assert response.status_code == 404


def test_create_user():
    payload = {"name": "Ivan Tester", "job": "QA Automation Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert "id" in body


def test_update_user():
    payload = {"name": "Ivan Tester", "job": "Senior QA Automation Engineer"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["job"] == payload["job"]


def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)

    assert response.status_code == 204
