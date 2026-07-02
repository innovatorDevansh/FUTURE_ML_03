import streamlit as st
import pandas as pd

from src.ui.sidebar import render_sidebar
from src.ui.dashboard import dashboard

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide",
)

try:

    df = pd.read_csv(
        "cache/final_resume_ranking.csv"
    )

except FileNotFoundError:

    st.error(
        "Run Step 8 first. final_resume_ranking.csv not found."
    )

    st.stop()

category, recommendation, search = render_sidebar(df)

filtered_df = df.copy()

if category != "All":

    filtered_df = filtered_df[
        filtered_df["category"] == category
    ]

if recommendation != "All":

    filtered_df = filtered_df[
        filtered_df["recommendation"] == recommendation
    ]

if search:

    filtered_df = filtered_df[
        filtered_df["category"]
        .str.contains(
            search,
            case=False,
            na=False,
        )
    ]

dashboard(filtered_df)