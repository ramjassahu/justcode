# Atomberg AI Agent: YouTube Share of Voice Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://justcode-for-fun.streamlit.app/)

An interactive web application that analyzes YouTube search results to quantify the Share of Voice (SoV) for Atomberg and its competitors, built for the Atomberg AI/ML internship challenge.

---

## 🚀 Live Demo

You can access the live, deployed application here:

**[https://justcode-for-fun.streamlit.app/](https://justcode-for-fun.streamlit.app/)**

---

## 🎯 Project Overview

This project is an AI agent designed to provide actionable market intelligence by:

-   Searching YouTube for user-defined keywords (e.g., 'smart fan', 'BLDC fan').
-   Scraping and analyzing data from the top N search results.
-   Calculating an **Engagement-Weighted Share of Voice (E-SoV)** to measure market influence accurately.
-   Performing **Ensemble Sentiment Analysis** to determine the Share of Positive Voice (SoPV).
-   Displaying all findings in an interactive and easy-to-understand dashboard.

---

## ✨ Features

-   **Dynamic User Controls**: Configure keywords and the number of videos to analyze directly in the app.
-   **Engagement-Weighted SoV**: A custom metric that prioritizes mentions in high-engagement videos for a more accurate SoV score.
-   **Ensemble Sentiment Analysis**: Combines VADER and TextBlob models for a more robust and nuanced understanding of user sentiment.
-   **Interactive Visualizations**: Uses Plotly to create modern, interactive charts that are easy to explore.
-   **Performance Caching**: Caches analysis results to provide a fast and smooth user experience on repeated queries.
-   **Secure API Key Management**: Uses Streamlit Secrets to keep API keys safe in the deployed application.

---

## 🛠️ Tech Stack

| Technology              | Purpose                                                              |
| :---------------------- | :------------------------------------------------------------------- |
| **Python** | Core programming language for the backend and analysis pipeline.     |
| **Streamlit** | Framework used to build and deploy the interactive web dashboard.    |
| **YouTube Data API v3** | For reliable and compliant collection of YouTube search and video data. |
| **Pandas** | For efficient data manipulation, cleaning, and aggregation.          |
| **VADER & TextBlob** | AI libraries used for the ensemble sentiment analysis model.         |
| **Plotly** | For creating interactive, modern data visualizations.                |
| **Git & GitHub** | For version control and as the source for deployment.                |

---

## 🔧 Setup & Local Execution

### Prerequisites

-   Python 3.8+
-   A YouTube Data API v3 Key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ramjassahu/justcode.git](https://github.com/ramjassahu/justcode.git)
    cd justcode
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Add your API Key (for local use):**
    To run the app locally, you need to create a secrets file.
    -   Create a folder named `.streamlit` in your project's root directory.
    -   Inside it, create a file named `secrets.toml`.
    -   Add your API key to this file in the following format:
        ```toml
        API_KEY = "your_youtube_api_key_goes_here"
        ```

### Running the App

Once the setup is complete, run the following command in your terminal:

```bash
streamlit run app.py
