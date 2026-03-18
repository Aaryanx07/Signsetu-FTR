import pytest
from api_client import VideoAPI
from config import USER1_HEADERS

api = VideoAPI()


@pytest.fixture
def video():

    response = api.create_video(USER1_HEADERS)

    assert response.status_code == 201

    video_id = response.json()["id"]

    yield video_id

    api.delete_video(video_id, USER1_HEADERS)