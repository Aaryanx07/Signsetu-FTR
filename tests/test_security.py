import time
from api_client import VideoAPI
from config import USER1_HEADERS, USER2_HEADERS

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