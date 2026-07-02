"""
Resume NLP Preprocessor
"""

import pandas as pd
import spacy

from src.preprocessing.cleaner import TextCleaner
from src.utils.logger import get_logger

logger = get_logger(__name__)

nlp = spacy.load("en_core_web_sm")


class ResumePreprocessor:

    def preprocess(self, text: str) -> str:
        """
        Clean + Lemmatize + Remove Stopwords
        """

        cleaned = TextCleaner.clean(text)

        doc = nlp(cleaned)

        tokens = []

        for token in doc:

            if token.is_stop:
                continue

            if token.is_space:
                continue

            if len(token.text) < 2:
                continue

            tokens.append(token.lemma_)

        return " ".join(tokens)

    def process_dataframe(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info("Cleaning resumes...")

        df["cleaned_text"] = df["text"].apply(
            self.preprocess
        )

        return df