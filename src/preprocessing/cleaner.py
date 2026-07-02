"""
Text cleaning utilities.
"""

import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:
        """
        Basic text cleaning.
        """

        if not isinstance(text, str):
            return ""

        # lowercase
        text = text.lower()

        # remove urls
        text = re.sub(r"http\S+|www\S+", " ", text)

        # remove email
        text = re.sub(r"\S+@\S+", " ", text)

        # remove phone numbers
        text = re.sub(r"\+?\d[\d\s\-]{8,}\d", " ", text)

        # remove punctuation
        text = re.sub(r"[^\w\s]", " ", text)

        # remove digits
        text = re.sub(r"\d+", " ", text)

        # remove extra spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()