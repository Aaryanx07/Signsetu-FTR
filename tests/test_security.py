import time
import base64
from api_client import VideoAPI
from config import USER1_HEADERS, USER2_HEADERS, BASE_URL
import random
import requests

api = VideoAPI()


def test_owner_can_access_captions(video):

    api.process_captions(video, USER1_HEADERS)

    time.sleep(2)

    response = api.get_captions(video, USER1_HEADERS)

    assert response.status_code in [200, 202, 404]


def test_unauthorized_candidate_access(video):

    api.process_captions(video, USER1_HEADERS)

    time.sleep(2)

    response = api.get_captions(video, USER2_HEADERS)

    assert response.status_code in [403, 404], \
        f"BUG: unauthorized access allowed ({response.status_code})"


def test_auth_token_predictability():

    url = f"{BASE_URL}/api/auth"

    random_candidate_id = random.randint(100000, 999999)

    headers = {
        "Content-Type": "application/json",
        "X-Candidate-ID": str(random_candidate_id)
    }

    response = requests.post(url, headers=headers)

    assert response.status_code in [200, 201]

    data = response.json()

    assert "token" in data, "BUG: token not returned by authentication API"
    assert "expiresAt" in data, "BUG: expiresAt not returned in authentication response"

    token = data["token"]

    decoded = base64.b64decode(token).decode()

    assert decoded.isdigit(), \
    "BUG: token is not Base64 encoded timestamp"

    decoded_timestamp = int(decoded)

    expires_at = int(data["expiresAt"])

    assert decoded_timestamp != expires_at, \
    "BUG: decoded token timestamp matches expiresAt"

def test_expired_token_access(video):
    
    url = f"{BASE_URL}/api/auth"

    random_candidate_id = random.randint(100000, 999999)
    use_candidate_id = str(random_candidate_id)
    
    headers = {
        "Content-Type": "application/json",
        "X-Candidate-ID": use_candidate_id
    }

    response = requests.post(url, headers=headers)

    assert response.status_code in [200, 201]

    data = response.json()

    token = data["token"]

    time.sleep(5)

    video_url = f"{BASE_URL}/api/videos/{video}"

    headers = {
        "Authorization": f"Bearer {token}",
        "X-Candidate-ID": use_candidate_id
    }
    response = requests.get(video_url, headers=headers)

    assert response.status_code == 200, \
        f"BUG: Token expired very quickly, Expected(401), Got({response.status_code})"