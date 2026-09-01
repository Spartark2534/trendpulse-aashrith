"""
TrendPulse - Task 4: Visualization
Creates a visual dashboard from the processed data.

Input:
    data/processed_trends.csv
    outputs/keyword_frequency.csv

Output:
    outputs/trend_dashboard.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = Path("data/processed_trends.csv")
KEYWORD_FILE = Path("outputs/keyword_frequency.csv")
OUTPUT_FILE = Path("outputs/trend_dashboard.png")


def create_dashboard():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"{DATA_FILE} not found. Run task2_data_processing.py first."
        )

    df = pd.read_csv(DATA_FILE)
    keywords = (
        pd.read_csv(KEYWORD_FILE)
        if KEYWORD_FILE.exists()
        else pd.DataFrame(columns=["keyword", "frequency"])
    )

    fig = plt.figure(figsize=(14, 10))

    # 1. Top stories by engagement.
    ax1 = plt.subplot(2, 2, 1)
    top_stories = df.nlargest(10, "engagement_score").sort_values(
        "engagement_score"
    )
    ax1.barh(top_stories["title"].str.slice(0, 45), top_stories["engagement_score"])
    ax1.set_title("Top 10 Stories by Engagement")
    ax1.set_xlabel("Engagement Score")
    ax1.tick_params(axis="y", labelsize=8)

    # 2. Top domains.
    ax2 = plt.subplot(2, 2, 2)
    domain_data = (
        df.groupby("domain")["engagement_score"]
        .sum()
        .nlargest(10)
        .sort_values()
    )
    ax2.barh(domain_data.index, domain_data.values)
    ax2.set_title("Top Domains by Total Engagement")
    ax2.set_xlabel("Engagement Score")
    ax2.tick_params(axis="y", labelsize=8)

    # 3. Score distribution.
    ax3 = plt.subplot(2, 2, 3)
    ax3.hist(df["score"], bins=12)
    ax3.set_title("Story Score Distribution")
    ax3.set_xlabel("Score")
    ax3.set_ylabel("Number of Stories")

    # 4. Most common keywords.
    ax4 = plt.subplot(2, 2, 4)
    top_keywords = keywords.head(10).sort_values("frequency")
    ax4.barh(top_keywords["keyword"], top_keywords["frequency"])
    ax4.set_title("Most Common Trending Keywords")
    ax4.set_xlabel("Frequency")

    fig.suptitle("TrendPulse — Live Hacker News Trend Dashboard", fontsize=18)
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_FILE, dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"Dashboard saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    create_dashboard()
