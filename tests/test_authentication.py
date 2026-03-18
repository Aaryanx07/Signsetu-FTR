import requests
import random
from config import BASE_URL

def test_authentication_success():

    url = f"{BASE_URL}/api/auth"

    random_candidate_id = random.randint(100000, 999999)

    headers = {
        "Content-Type": "application/json",
        "X-Candidate-ID": str(random_candidate_id)
    }

    response = requests.post(url, headers=headers)

    assert response.status_code in [200, 201]

    data = response.json()

    assert "token" in data, \
        "BUG: authentication did not return session token"

    assert isinstance(data["token"], str)

def test_auth_missing_candidate_id():

    url = f"{BASE_URL}/api/auth"

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers)

    assert response.status_code in [400, 401], \
        f"BUG: authentication allowed missing candidate id ({response.status_code})"

def test_auth_empty_candidate_id():

    url = f"{BASE_URL}/api/auth"

    headers = {
        "Content-Type": "application/json",
        "X-Candidate-ID": ""
    }

    response = requests.post(url, headers=headers)

    assert response.status_code in [400, 401], \
        f"BUG: authentication accepted empty candidate id ({response.status_code})"

def test_auth_extra_headers():

    url = f"{BASE_URL}/api/auth"

    random_candidate_id = random.randint(100000, 999999)

    headers = {
        "Content-Type": "application/json",
        "X-Candidate-ID": str(random_candidate_id),
        "X-Test-Header": "extra"
    }

    response = requests.post(url, headers=headers)

    assert response.status_code in [200, 201], \
        f"Unexpected response when extra headers provided ({response.status_code})"
    
