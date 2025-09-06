# Atomberg AI Agent: YouTube Share of Voice Analysis

This project is an AI agent designed to analyze YouTube search results to quantify the Share of Voice (SoV) for Atomberg and its competitors in the 'smart fan' market, as per the AI/ML internship problem statement.

## Features

-   **Data Collection**: Searches YouTube for specified keywords and scrapes data from the top N results.
-   **Brand Mention Analysis**: Identifies mentions of Atomberg and key competitors in video titles, descriptions, and comments.
-   **Engagement-Weighted SoV**: Calculates a custom "Engagement-Weighted Share of Voice" (E-SoV) metric that prioritizes mentions in high-engagement videos.
-   **Sentiment Analysis**: Performs sentiment analysis on comments mentioning each brand to calculate a "Share of Positive Voice" (SoPV).
-   **Report Generation**: Automatically generates and saves pie charts (for E-SoV) and bar charts (for SoPV) for each keyword.

## Setup Instructions

**1. Clone the Repository**

```bash
git clone <your-repo-url>
cd atomberg_sov_project
```

**2. Create a Virtual Environment**

It's highly recommended to use a virtual environment to manage dependencies.

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

**3. Install Dependencies**

Install all the required Python libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

**4. Add Your API Key**

You need a YouTube Data API v3 key from the Google Cloud Console.

-   Open the `config.py` file.
-   Find the line `API_KEY = "YOUR_API_KEY"`.
-   Replace `"YOUR_API_KEY"` with the actual key you generated.

## How to Run

Once the setup is complete, you can run the entire analysis pipeline with a single command:

```bash
python main.py
```

The script will:
1.  Fetch data from YouTube (this may take a few minutes).
2.  Save the raw data to `output/youtube_raw_data.csv`.
3.  Analyze the data for mentions and sentiment.
4.  Save the detailed analysis to `output/youtube_analysis_data.csv`.
5.  Print the final E-SoV and SoPV metrics to your console.
6.  Save the visual charts as PNG files in the `output/` directory.

## Project Structure

-   `main.py`: The main entry point to run the application.
-   `config.py`: Configuration file for API keys, keywords, competitors, and scoring weights.
-   `youtube_scraper.py`: Module responsible for fetching all data from the YouTube API.
-   `analyzer.py`: Module for performing the core data analysis (mention counting, sentiment analysis, SoV calculation).
-   `report_generator.py`: Module to create and save the data visualizations.
-   `requirements.txt`: A list of all project dependencies.
-   `output/`: A directory where all output files (data and charts) are saved.