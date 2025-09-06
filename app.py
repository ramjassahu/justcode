import streamlit as st
import pandas as pd
import config
from main import run_full_analysis
from report_generator import plot_sov_pie_chart, plot_sopv_bar_chart

# --- Page Configuration ---
st.set_page_config(page_title="Atomberg SoV Dashboard", page_icon="💡", layout="wide")

# --- App State ---
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None

# --- Header ---
st.title("💡 Atomberg AI Agent: Share of Voice Dashboard")
st.markdown("An interactive tool to analyze Atomberg's market presence on YouTube using AI-powered sentiment analysis.")

# --- Sidebar Controls ---
st.sidebar.header("🔬 Analysis Controls")
default_keywords = "smart fan\nbest BLDC fan\nAtomberg fan review"
user_keywords = st.sidebar.text_area("Keywords to search (one per line)", default_keywords, height=100)
keywords_list = [kw.strip() for kw in user_keywords.split('\n') if kw.strip()]
n_results = st.sidebar.slider("Videos to analyze per keyword", 5, 50, 20, help="Higher numbers are more accurate but take longer.")

# --- Main Logic ---
if st.sidebar.button("🚀 Run Analysis", type="primary"):
    try:
        api_key_to_use = st.secrets["API_KEY"]
    except KeyError:
        st.error("API_KEY not found in Streamlit Secrets. Please add it for the deployed app.")
        st.stop()

    if not keywords_list:
        st.error("Please enter at least one keyword.")
    else:
        with st.spinner(f"🔍 Analyzing {len(keywords_list) * n_results} videos... Please wait."):
            results = run_full_analysis(tuple(keywords_list), n_results, api_key_to_use)
            st.session_state.analysis_results = results
        st.success("✅ Analysis Complete!")
        st.balloons()

# --- Display Results ---
if st.session_state.analysis_results:
    results = st.session_state.analysis_results
    keyword_tabs = st.tabs([f"'{kw}'" for kw in results.keys()])

    for i, keyword in enumerate(results.keys()):
        with keyword_tabs[i]:
            metrics = results[keyword]
            e_sov_data = {k: v for k, v in metrics['e_sov'].items() if v > 0}
            mentioned_brands = list(e_sov_data.keys())

            st.header(f"Results for Keyword: '{keyword}'")
            col1, col2, col3 = st.columns(3)
            col1.metric(label="Atomberg's E-SoV", value=f"{e_sov_data.get('Atomberg', 0):.1f}%")
            col2.metric(label="Atomberg's Positive Voice", value=f"{metrics['sopv'].get('Atomberg', 0):.1f}%")
            if mentioned_brands:
                leader = max(e_sov_data, key=e_sov_data.get)
                col3.metric(label="Market Leader", value=f"{leader} ({e_sov_data[leader]:.1f}%)")
            st.divider()

            chart_col1, chart_col2 = st.columns(2)
            with chart_col1:
                sov_fig = plot_sov_pie_chart(e_sov_data, keyword)
                if sov_fig: st.plotly_chart(sov_fig, use_container_width=True)
                else: st.warning("No brand mentions found.")
            with chart_col2:
                sopv_fig = plot_sopv_bar_chart(metrics['sopv'], mentioned_brands)
                if sopv_fig: st.plotly_chart(sopv_fig, use_container_width=True)
                else: st.warning("No mentions found.")
else:
    st.info("Configure your search in the sidebar and click 'Run Analysis' to begin.")