import requests
from config import BASE_URL, USER1_HEADERS
from api_client import VideoAPI

api = VideoAPI()


def test_invalid_limit():

    url = f"{BASE_URL}/api/videos?limit=-1"

    response = requests.get(url, headers=USER1_HEADERS)

    assert response.status_code == 400, \
        f"BUG: invalid limit accepted ({response.status_code})"


def test_invalid_video_id_delete():

    url = f"{BASE_URL}/api/videos/"

    response = requests.delete(url, headers=USER1_HEADERS)

    assert response.status_code in [400,404], \
        f"BUG: missing path parameter allowed ({response.status_code})"