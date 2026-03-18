from api_client import VideoAPI
from config import USER1_HEADERS

api = VideoAPI()

def test_successful_video_deletion(video):

    response = api.delete_video(video, USER1_HEADERS)

    assert response.status_code == 204

def test_delete_invalid_video():

    invalid_id = "invalid-video-id"

    response = api.delete_video(invalid_id, USER1_HEADERS)

    assert response.status_code == 404, \
        f"BUG: invalid delete returned {response.status_code}"

def test_double_delete(video):

    first = api.delete_video(video, USER1_HEADERS)

    assert first.status_code == 204

    second = api.delete_video(video, USER1_HEADERS)

    assert second.status_code == 404, \
        f"BUG: double delete allowed ({second.status_code})"