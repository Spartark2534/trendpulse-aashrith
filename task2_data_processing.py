"""
TrendPulse - Task 2: Data Processing
Cleans the raw Hacker News data and creates analysis-ready CSV data.

Input:
    data/raw_trends.json

Output:
    data/processed_trends.csv
"""

from pathlib import Path
import json
import re
from urllib.parse import urlparse

import pandas as pd

INPUT_FILE = Path("data/raw_trends.json")
OUTPUT_FILE = Path("data/processed_trends.csv")

STOP_WORDS = {
    "the", "a", "an", "and", "or", "to", "of", "in", "for", "on", "with",
    "from", "is", "are", "be", "this", "that", "how", "why", "what",
    "new", "show", "ask", "hn", "you", "your", "we", "it", "as", "by",
    "at", "about", "into", "than", "more", "can", "will", "has", "have"
}


def extract_domain(url):
    if not url:
        return "Hacker News"
    try:
        domain = urlparse(url).netloc.lower()
        return domain.replace("www.", "") or "Unknown"
    except ValueError:
        return "Unknown"


def clean_title(title):
    title = str(title or "").strip()
    title = re.sub(r"\s+", " ", title)
    return title


def extract_keywords(title):
    words = re.findall(r"[A-Za-z][A-Za-z0-9+#.-]{2,}", title.lower())
    return [word for word in words if word not in STOP_WORDS]


def process_data():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"{INPUT_FILE} not found. Run task1_data_collection.py first."
        )

    raw = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    stories = raw.get("stories", [])

    rows = []

    for story in stories:
        title = clean_title(story.get("title"))
        score = int(story.get("score") or 0)
        comments = int(story.get("descendants") or 0)
        timestamp = story.get("time")

        created_at = pd.to_datetime(timestamp, unit="s", utc=True, errors="coerce")
        age_hours = (
            (pd.Timestamp.now(tz="UTC") - created_at).total_seconds() / 3600
            if pd.notna(created_at)
            else None
        )

        # A simple engagement metric combining votes and comments.
        engagement_score = score + (comments * 2)

        rows.append(
            {
                "id": story.get("id"),
                "title": title,
                "author": story.get("by", "unknown"),
                "score": score,
                "comments": comments,
                "engagement_score": engagement_score,
                "domain": extract_domain(story.get("url")),
                "created_at": created_at.isoformat() if pd.notna(created_at) else None,
                "age_hours": round(max(age_hours, 0), 2) if age_hours is not None else None,
                "keywords": ", ".join(extract_keywords(title)),
                "url": story.get("url")
                or f"https://news.ycombinator.com/item?id={story.get('id')}",
            }
        )

    df = pd.DataFrame(rows)

    # Remove duplicates, missing titles, and invalid numeric values.
    df = df.drop_duplicates(subset="id")
    df = df[df["title"].str.len() > 0]
    df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
    df["comments"] = pd.to_numeric(df["comments"], errors="coerce").fillna(0).astype(int)
    df["engagement_score"] = pd.to_numeric(
        df["engagement_score"], errors="coerce"
    ).fillna(0).astype(int)

    df = df.sort_values("engagement_score", ascending=False).reset_index(drop=True)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Processed {len(df)} records.")
    print(f"Saved cleaned data to {OUTPUT_FILE}")
    print("\nTop 5 stories:")
    print(df[["title", "score", "comments", "engagement_score"]].head().to_string(index=False))


if __name__ == "__main__":
    process_data()
