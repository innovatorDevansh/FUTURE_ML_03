import streamlit as st


def render_sidebar(df):
    """
    Render dashboard sidebar.
    """

    st.sidebar.title("Filters")

    categories = sorted(df["category"].dropna().unique())

    category = st.sidebar.selectbox(
        "Category",
        ["All"] + categories
    )

    recommendations = sorted(
        df["recommendation"].dropna().unique()
    )

    recommendation = st.sidebar.selectbox(
        "Recommendation",
        ["All"] + recommendations
    )

    search = st.sidebar.text_input(
        "Search Category"
    )

    return category, recommendation, search