import requests
from django.conf import settings

YOUTUBE_API_URL = ("https://www.googleapis.com/youtube/v3/videos")

def fetch_youtube_video(video_id):
    params = {
        "part":"snippet,contentDetails,status",
        "id":video_id,
        "key": settings.YOUTUBE_API_KEY

    }
    response = requests.get(YOUTUBE_API_URL, params, timeout=15,)
    response.raise_for_status()
    data = response.json()
    items = data.get("items", [])
    if not items:
        return None
    video = items[0]
    snippet = video.get("snippet", {})
    content_details = video.get("contentDetails", {})
    status = video.get("status", {})
    thumbnails = snippet.get("thumbnails", {})
    thumbnail = (thumbnails.get("high",{}).get('url', ""))
    return {
        "title": snippet.get('title', ""),
        "description": snippet.get("description", ""),
        "thumbnail_url": thumbnail,
        "channel_title": snippet.get("channelTitle", ""),
        "duration": content_details.get("duration", ""),
        "privacy_status": status.get("privacyStatus", ""),
        "embeddable": status.get("embeddable", False),

  }

