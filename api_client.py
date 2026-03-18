import requests
from config import BASE_URL


class VideoAPI:

    def create_video(self, headers, title="Automation Test Video"):

        url = f"{BASE_URL}/api/videos"

        payload = {"title": title}

        return requests.post(url, json=payload, headers=headers)


    def get_video(self, video_id, headers):

        url = f"{BASE_URL}/api/videos/{video_id}"

        return requests.get(url, headers=headers)


    def process_captions(self, video_id, headers):

        url = f"{BASE_URL}/api/videos/{video_id}/process-captions"

        return requests.post(url, headers=headers)


    def get_captions(self, video_id, headers):

        url = f"{BASE_URL}/api/captions?videoId={video_id}"

        return requests.get(url, headers=headers)


    def delete_video(self, video_id, headers):

        url = f"{BASE_URL}/api/videos/{video_id}"

        return requests.delete(url, headers=headers)