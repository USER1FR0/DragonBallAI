import requests
from configs.config import BaseConfig

API_KEY = BaseConfig.YOUTUBE_API_KEY
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

PRESET_QUERIES = [
    "Dragon Ball Z peleas épicas",
    "Dragon Ball Super momentos épicos",
    "Dragon Ball Z transformaciones",
    "Dragon Ball teorías",
    "Dragon Ball Z capitulos completos español",
    "Dragon Ball highlights",
]

class YoutubeService:

    @staticmethod
    def search(query, max_results=12):
        # Forzar que siempre sea sobre Dragon Ball
        safe_query = f"{query} Dragon Ball" if "dragon ball" not in query.lower() else query
        try:
            r = requests.get(SEARCH_URL, params={
                "part": "snippet",
                "q": safe_query,
                "type": "video",
                "maxResults": max_results,
                "key": API_KEY,
                "relevanceLanguage": "es",
            }, timeout=8)
            r.raise_for_status()
            items = r.json().get("items", [])
            return [
                {
                    "id": v["id"]["videoId"],
                    "title": v["snippet"]["title"],
                    "thumbnail": v["snippet"]["thumbnails"]["medium"]["url"],
                    "channel": v["snippet"]["channelTitle"],
                }
                for v in items if v["id"].get("videoId")
            ]
        except Exception as e:
            print(f"[YoutubeService] {e}")
            return []

    @staticmethod
    def get_presets():
        return PRESET_QUERIES