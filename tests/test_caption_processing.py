import time
from api_client import VideoAPI
from config import USER1_HEADERS

api = VideoAPI()


def test_duplicate_caption_processing(video):

    first = api.process_captions(video, USER1_HEADERS)

    assert first.status_code in [200, 202]

    second = api.process_captions(video, USER1_HEADERS)

    assert second.status_code in [400, 409], \
        f"BUG: duplicate processing allowed ({second.status_code})"


def test_fetch_captions_while_processing(video):

    api.process_captions(video, USER1_HEADERS)

    response = api.get_captions(video, USER1_HEADERS)

    assert response.status_code in [202, 404], \
        "BUG: captions endpoint returned invalid response"