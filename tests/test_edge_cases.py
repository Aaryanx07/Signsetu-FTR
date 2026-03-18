import requests
from config import BASE_URL, USER1_HEADERS

def test_valid_limit_parameter():

    url = f"{BASE_URL}/api/videos?limit=5"

    response = requests.get(url, headers=USER1_HEADERS)

    assert response.status_code == 200

def test_invalid_limit_parameter():

    url = f"{BASE_URL}/api/videos?limit=-1"

    response = requests.get(url, headers=USER1_HEADERS)

    assert response.status_code == 400, \
        f"BUG: invalid limit accepted ({response.status_code})"

def test_missing_video_id_delete():

    url = f"{BASE_URL}/api/videos/"

    response = requests.delete(url, headers=USER1_HEADERS)

    assert response.status_code in [400,404], \
        f"BUG: missing path parameter allowed ({response.status_code})"