from api_client import VideoAPI
from config import USER1_HEADERS

api = VideoAPI()


def test_custom_title():

    title = "QA Custom Title"

    response = api.create_video(USER1_HEADERS, title)

    assert response.status_code == 201

    returned_title = response.json()["title"]

    assert returned_title == title, \
        f"BUG: custom title ignored ({returned_title})"


def test_candidate_id_matches_header():

    response = api.create_video(USER1_HEADERS)

    candidate_id = response.json()["candidate_id"]

    assert candidate_id == USER1_HEADERS["X-Candidate-ID"], \
        "BUG: candidate id mismatch"