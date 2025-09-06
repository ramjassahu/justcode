import streamlit as st
import config
from youtube_scraper import fetch_data_for_keywords
from analyzer import analyze_data

@st.cache_data(ttl=3600)
def run_full_analysis(keywords, n_results, api_key):
    """
    This function runs the entire pipeline and returns the final metrics.
    It's cached to avoid re-running expensive API calls and analysis.
    """
    print("--- Cache miss! Running full analysis pipeline. ---")
    
    raw_df = fetch_data_for_keywords(
        api_key=api_key,
        keywords=keywords,
        n_results=n_results,
        max_comments=config.MAX_COMMENTS
    )
    if raw_df is None or raw_df.empty:
        return None

    _, final_metrics = analyze_data(
        raw_df,
        config.COMPETITORS,
        config.MENTION_WEIGHTS
    )
    return final_metrics