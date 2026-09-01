1. TrendPulse

TrendPulse is a Python-based data pipeline that collects live trending stories, cleans and processes the data, finds useful insights, and turns those insights into visualizations.

I built this project to understand how a complete data pipeline works in practice — starting with getting data from an API and ending with a dashboard that makes the results easier to understand.

The project is divided into four stages:

Collect → Process → Analyze → Visualize . 
______________________________________________________________________________________________________________________________________________________________________________________

2.  What is TrendPulse?

TrendPulse uses the public Hacker News API to collect currently trending stories.

For each story, the pipeline works with information such as:

- Story title
- Author
- Score
- Number of comments
- Website/domain
- Creation time
- Story URL

The collected data then passes through three more stages where it is cleaned, analyzed, and visualized.

______________________________________________________________________________________________________________________________________________________________________________________

3.  How the Pipeline Works

```text
        Hacker News API
               │
               ▼
   ┌──────────────────────┐
   │ 1. Data Collection   │
   └──────────┬───────────┘
              │
              ▼
       raw_trends.json
              │
              ▼
   ┌──────────────────────┐
   │ 2. Data Processing   │
   └──────────┬───────────┘
              │
              ▼
     processed_trends.csv
              │
              ▼
   ┌──────────────────────┐
   │ 3. Data Analysis     │
   └──────────┬───────────┘
              │
              ▼
     Analysis & Keywords
              │
              ▼
   ┌──────────────────────┐
   │ 4. Visualization     │
   └──────────┬───────────┘
              │
              ▼
      Trend Dashboard
```

_________________________________________________________________________________________________________________________________________________________________________________

4.  Project Structure

```text
trendpulse-aashrith/
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
│
├── requirements.txt
├── README.md
├── .gitignore
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

_______________________________________________________________________________________________________________________________________________________________

-> Data Collection

**File:** `task1_data_collection.py`

The first step is to collect live data.

The script connects to the Hacker News API, gets the current top stories, and then retrieves the details for each story.

It also handles failed requests so that one unavailable story doesn't stop the entire pipeline.

The collected information is saved as:

```text
data/raw_trends.json
```

This file represents the raw data before any major processing is done.

______________________________________________________________________________________________________________________________________________________________________________

-> Data Processing

**File:** `task2_data_processing.py`

Once the raw data is collected, it needs to be cleaned before it can be analyzed.

This stage:

- Cleans story titles
- Removes duplicate stories
- Handles missing values
- Extracts the website domain
- Calculates the age of each story
- Extracts useful keywords
- Creates an engagement score
- Sorts the stories based on engagement
__________________________________________________________________________________________________________________________________________________________________________
5.  Engagement Score

I used a simple formula to estimate how much attention a story is receiving:

```text
Engagement Score = Score + (Comments × 2)
```

Comments are given extra weight because they represent active interaction with a story.

The processed data is saved as:

```text
data/processed_trends.csv
```

---

-> Data Analysis

**File:** `task3_analysis.py`

After cleaning the data, the next step is to find patterns and useful information.

The analysis looks at:

- Total number of stories
- Total scores
- Total comments
- Average score
- Average comments
- Most-engaged story
- Popular domains
- Frequently occurring keywords

The results are saved in:

```text
outputs/trend_analysis.json
outputs/keyword_frequency.csv
```

This makes the analysis results available separately from the original dataset.

_______________________________________________________________________________________________________________________________________________________________________________

-> Data Visualization

**File:** `task4_visualization.py`

The final stage turns the analysis into something easier to understand visually.

The dashboard contains four main charts:

6.  Top 10 Stories by Engagement

Shows which stories received the most overall engagement.

7.  Top Domains

Shows which websites contributed stories with the highest total engagement.

8.  📈 Story Score Distribution

Shows how the scores are distributed across the collected stories.

9.  🔑 Common Keywords

Shows the keywords that appeared most frequently in the story titles.

The final dashboard is saved as:

```text
outputs/trend_dashboard.png
```

______________________________________________________________________________________________________________________________________________________________________________________

10.  Technologies Used

- **Python** – Main programming language
- **Requests** – Used to communicate with the Hacker News API
- **Pandas** – Used for cleaning, processing, and analyzing data
- **Matplotlib** – Used to create the dashboard
- **JSON** – Used to store the raw API response
- **CSV** – Used to store the processed dataset
- **Git & GitHub** – Used for version control and project hosting

_______________________________________________________________________________________________________________________________________________________________________________________

11.  How to Run the Project

STEP 1. Clone the repository

```bash
git clone https://github.com/Spartark2534/trendpulse-aashrith.git
```

Move into the project folder:

```bash
cd trendpulse-aashrith
```

STEP 2. Create a virtual environment

On Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

STEP 3. Install the required libraries

```bash
pip install -r requirements.txt
```

STEP 4. Run the pipeline

Run the four scripts in this order:

```bash
python task1_data_collection.py
```

```bash
python task2_data_processing.py
```

```bash
python task3_analysis.py
```

```bash
python task4_visualization.py
```

Each stage uses the output generated by the previous stage.

---

12.  Example Run

During my test run, the pipeline collected and processed **49 live stories**.

Some of the results were:

```text
Stories analyzed : 49
Total score      : 10163
Total comments   : 4090
Average score    : 207.41
Average comments : 83.47
```

The highest-engagement story in that particular run was:

```text
"I just chose words carefully"
```

Since the project uses live data from Hacker News, the results will naturally be different when the pipeline is run again.

---

->  What I Learned

Building TrendPulse helped me understand how the different parts of a data pipeline fit together.

Some of the main things I worked with were:

- Calling a REST API from Python
- Working with JSON data
- Cleaning real-world data
- Handling missing and duplicate data
- Creating new metrics from existing data
- Extracting keywords from text
- Using Pandas for data analysis
- Creating charts with Matplotlib
- Organizing a multi-stage Python project
- Using Git for version control
- Publishing a project on GitHub

---

--> Possible Improvements

There are several ways I could extend TrendPulse in the future:

- Collect data from multiple sources instead of just Hacker News
- Store historical data so trends can be compared over time
- Add sentiment analysis to story titles
- Build an interactive dashboard
- Schedule the pipeline to run automatically
- Add more advanced trend detection
- Store the data in a database instead of files

---

About Me

**Aashrith**

GitHub: [@Spartark2534](https://github.com/Spartark2534)

TrendPulse was built as a hands-on project to practice Python, data processing, analysis, visualization, and GitHub while working with a real-world live data source.
