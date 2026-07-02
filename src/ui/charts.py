import plotly.express as px
import streamlit as st


def ats_distribution(df):

    fig = px.histogram(
        df,
        x="ats_score",
        nbins=20,
        title="ATS Score Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def category_distribution(df):

    category_df = (
        df["category"]
        .value_counts()
        .reset_index()
    )

    category_df.columns = [
        "Category",
        "Count"
    ]

    fig = px.bar(
        category_df.head(10),
        x="Category",
        y="Count",
        title="Top Categories"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def recommendation_chart(df):

    rec_df = (
        df["recommendation"]
        .value_counts()
        .reset_index()
    )

    rec_df.columns = [
        "Recommendation",
        "Count"
    ]

    fig = px.pie(
        rec_df,
        names="Recommendation",
        values="Count",
        title="Recommendation Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )