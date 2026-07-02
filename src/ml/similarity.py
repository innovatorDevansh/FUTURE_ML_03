"""
Resume Similarity Module

Calculates TF-IDF Cosine Similarity between
all resumes and a job description.

Production Version
"""

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.utils.logger import get_logger

logger = get_logger(__name__)


class ResumeSimilarity:

    def __init__(self):

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=5000
        )

    def process_dataframe(
        self,
        df: pd.DataFrame,
        jd_text: str
    ) -> pd.DataFrame:
        """
        Calculate cosine similarity for every resume
        against one Job Description.

        Parameters
        ----------
        df : DataFrame
            Resume dataframe

        jd_text : str
            Cleaned Job Description

        Returns
        -------
        DataFrame
        """

        logger.info("Calculating TF-IDF vectors...")

        # Fill missing values
        df["cleaned_text"] = (
            df["cleaned_text"]
            .fillna("")
            .astype(str)
        )

        jd_text = "" if pd.isna(jd_text) else str(jd_text)

        # Build corpus
        corpus = df["cleaned_text"].tolist()

        corpus.append(jd_text)

        # Fit once
        tfidf_matrix = self.vectorizer.fit_transform(corpus)

        logger.info("Calculating cosine similarity...")

        # Last row is Job Description
        jd_vector = tfidf_matrix[-1]

        # All previous rows are resumes
        resume_vectors = tfidf_matrix[:-1]

        similarities = cosine_similarity(
            resume_vectors,
            jd_vector
        )

        df["cosine_score"] = (
            similarities.flatten() * 100
        ).round(2)

        logger.info("Cosine similarity completed.")

        return df