"""
TrendPulse - Task 3: Data Analysis
Analyzes the cleaned trending-story dataset.

Input:
    data/processed_trends.csv

Outputs:
    outputs/trend_analysis.json
    outputs/keyword_frequency.csv
"""

from collections import Counter
from pathlib import Path
import json
import re

import pandas as pd

INPUT_FILE = Path("data/processed_trends.csv")
ANALYSIS_FILE = Path("outputs/trend_analysis.json")
KEYWORD_FILE = Path("outputs/keyword_frequency.csv")


def analyze_data():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"{INPUT_FILE} not found. Run task2_data_processing.py first."
        )

    df = pd.read_csv(INPUT_FILE)

    keyword_counter = Counter()

    for keyword_string in df["keywords"].fillna(""):
        for keyword in keyword_string.split(","):
            keyword = keyword.strip()
            if keyword:
                keyword_counter[keyword] += 1

    keyword_df = pd.DataFrame(
        keyword_counter.most_common(20),
        columns=["keyword", "frequency"],
    )
    KEYWORD_FILE.parent.mkdir(parents=True, exist_ok=True)
    keyword_df.to_csv(KEYWORD_FILE, index=False)

    top_domains = (
        df.groupby("domain")
        .agg(
            stories=("id", "count"),
            total_score=("score", "sum"),
            total_comments=("comments", "sum"),
            total_engagement=("engagement_score", "sum"),
        )
        .sort_values("total_engagement", ascending=False)
        .head(10)
        .reset_index()
    )

    summary = {
        "total_stories": int(len(df)),
        "total_score": int(df["score"].sum()),
        "total_comments": int(df["comments"].sum()),
        "average_score": round(float(df["score"].mean()), 2),
        "average_comments": round(float(df["comments"].mean()), 2),
        "highest_engagement": int(df["engagement_score"].max()),
        "top_story": (
            df.loc[df["engagement_score"].idxmax(), "title"] if len(df) else None
        ),
        "top_domains": top_domains.to_dict(orient="records"),
        "top_keywords": keyword_df.to_dict(orient="records"),
    }

    ANALYSIS_FILE.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("\n=== TrendPulse Analysis ===")
    print(f"Stories analyzed : {summary['total_stories']}")
    print(f"Total score      : {summary['total_score']}")
    print(f"Total comments   : {summary['total_comments']}")
    print(f"Average score    : {summary['average_score']}")
    print(f"Average comments : {summary['average_comments']}")
    print(f"\nTop story:\n{summary['top_story']}")

    print("\nTop keywords:")
    print(keyword_df.head(10).to_string(index=False))

    print(f"\nSaved analysis to {ANALYSIS_FILE}")
    print(f"Saved keyword data to {KEYWORD_FILE}")


if __name__ == "__main__":
    analyze_data()
