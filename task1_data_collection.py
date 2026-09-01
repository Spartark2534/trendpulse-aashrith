"""
TrendPulse - Task 1: Data Collection
Fetches live trending stories from the Hacker News public API.

Output:
    data/raw_trends.json
"""

from pathlib import Path
from datetime import datetime, timezone
import json
import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"
OUTPUT_FILE = Path("data/raw_trends.json")
TOP_N = 50


def get_json(url: str):
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.json()


def collect_trending_data():
    print("Fetching live Hacker News trending stories...")

    story_ids = get_json(f"{BASE_URL}/topstories.json")[:TOP_N]
    stories = []

    for index, story_id in enumerate(story_ids, start=1):
        try:
            story = get_json(f"{BASE_URL}/item/{story_id}.json")
            if story and story.get("type") == "story":
                stories.append(story)
                print(f"[{index}/{len(story_ids)}] Collected: {story.get('title', 'Untitled')}")
        except requests.RequestException as exc:
            print(f"Skipping story {story_id}: {exc}")

    collected_at = datetime.now(timezone.utc).isoformat()

    payload = {
        "source": "Hacker News",
        "collected_at": collected_at,
        "count": len(stories),
        "stories": stories,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"\nSaved {len(stories)} stories to {OUTPUT_FILE}")


if __name__ == "__main__":
    collect_trending_data()
