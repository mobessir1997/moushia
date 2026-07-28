import re

YOUTUBE_URL_PATTERNS =[
  r"(?:youtube\.com/watch\?v=)([A-Za-z0-9_-]{11})",

    r"(?:youtu\.be/)([A-Za-z0-9_-]{11})",

    r"(?:youtube\.com/embed/)([A-Za-z0-9_-]{11})",

    r"(?:youtube\.com/shorts/)([A-Za-z0-9_-]{11})",
]

def extract_youtube_video_id(url):
    for pattern in YOUTUBE_URL_PATTERNS:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None