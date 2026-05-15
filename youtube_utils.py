from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def get_transcript(video_link):
    parsed = urlparse(video_link)

    if parsed.netloc not in ("www.youtube.com", "youtube.com", "youtu.be"):
        raise ValueError("Please enter a valid YouTube URL.")
    if parsed.netloc == "youtu.be":
        video_id = parsed.path[1:]
    else:
        video_id = parse_qs(parsed.query)["v"][0]
    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video_id)

    text = " ".join([snippet.text for snippet in transcript])

    return text
