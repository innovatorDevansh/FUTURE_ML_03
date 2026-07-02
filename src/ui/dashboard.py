import streamlit as st

from src.ui.charts import (
    ats_distribution,
    category_distribution,
    recommendation_chart,
)


def dashboard(df):

    st.title("📄 AI Resume Screening System")

    st.caption(
        "Machine Learning based Resume Screening & Candidate Ranking"
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Candidates",
        len(df)
    )

    col2.metric(
        "Highest ATS",
        round(df["ats_score"].max(), 2)
    )

    col3.metric(
        "Average ATS",
        round(df["ats_score"].mean(), 2)
    )

    col4.metric(
        "Highest Skill Score",
        round(df["skill_score"].max(), 2)
    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        ats_distribution(df)

    with c2:
        recommendation_chart(df)

    st.divider()

    category_distribution(df)

    st.divider()

    st.subheader("Candidate Ranking")

    st.dataframe(
        df[
            [
                "rank",
                "category",
                "ats_score",
                "skill_score",
                "cosine_score",
                "recommendation",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )