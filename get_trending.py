import os
import requests
import pandas as pd
from dotenv import load_dotenv
from insert_to_db import insert_videos

# Load API key from .env file
load_dotenv()
API_KEY = "AIzaSyAtdjS2xKcL44QHi_Oh54kgtRtVaX7iqGE"

# Base URL for YouTube Data API
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/videos"

# Parameters
params = {
    "part": "snippet,statistics",
    "chart": "mostPopular",
    "regionCode": "US",
    "key": API_KEY,
    "maxResults": 50
}

# Make the request
response = requests.get(YOUTUBE_API_URL, params=params)
data = response.json()

# Parse video info
videos = []
for item in data.get("items", []):
    snippet = item["snippet"]
    stats = item["statistics"]

    videos.append({
        "video_id": item["id"],
        "title": snippet["title"],
        "channel": snippet["channelTitle"],
        "category_id": snippet["categoryId"],
        "published_at": snippet["publishedAt"],
        "tags": snippet.get("tags", []),
        "view_count": stats.get("viewCount", 0),
        "like_count": stats.get("likeCount", 0),
        "comment_count": stats.get("commentCount", 0),
    })

insert_videos(videos)

if videos:
    print(f"✅ Parsed {len(videos)} videos")
    insert_videos(videos)
else:
    print("⚠️ No videos parsed! Skipping DB insert.")
