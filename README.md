# TrendPulse

TrendPulse is a small end-to-end Python data pipeline that:

1. Fetches live trending data
2. Cleans and transforms the data
3. Analyzes trends and engagement
4. Visualizes the results

The project uses the public Hacker News API as its live data source.

## Project structure

```text
trendpulse-yourname/
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw_trends.json
│   └── processed_trends.csv
│
└── outputs/
    ├── trend_analysis.json
    ├── keyword_frequency.csv
    └── trend_dashboard.png
```

## 1. Install Python

Use Python 3.10+ if possible.

Check:

```bash
python --version
```

## 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the pipeline

Run these four scripts in order:

```bash
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
```

## What each task demonstrates

### Task 1 — Data Collection
Connects to a live API, retrieves the current top stories, handles API errors, and stores raw JSON.

### Task 2 — Data Processing
Cleans titles, extracts domains, handles missing values, calculates age and engagement, removes duplicates, and creates a CSV.

### Task 3 — Analysis
Calculates summary statistics, identifies high-engagement stories, ranks domains, and extracts frequently occurring keywords.

### Task 4 — Visualization
Creates a dashboard showing:
- top stories by engagement
- top domains
- score distribution
- common trending keywords

## Data pipeline

```text
Hacker News API
      ↓
Task 1: Collection
      ↓
raw_trends.json
      ↓
Task 2: Processing
      ↓
processed_trends.csv
      ↓
Task 3: Analysis
      ↓
trend_analysis.json
keyword_frequency.csv
      ↓
Task 4: Visualization
      ↓
trend_dashboard.png
```

## GitHub submission

Create a public repository named:

```text
trendpulse-yourname
```

Upload the four required Python files.

You can also upload `requirements.txt` and `README.md`, plus example output files if your assignment allows them.

Your four submission links should look like:

```text
https://github.com/YOUR_USERNAME/trendpulse-yourname/blob/main/task1_data_collection.py
https://github.com/YOUR_USERNAME/trendpulse-yourname/blob/main/task2_data_processing.py
https://github.com/YOUR_USERNAME/trendpulse-yourname/blob/main/task3_analysis.py
https://github.com/YOUR_USERNAME/trendpulse-yourname/blob/main/task4_visualization.py
```

## Important

The four scripts are intentionally separate so that each task clearly demonstrates one stage of the pipeline. Do not combine them into one Python file if the assignment asks for four task files.
