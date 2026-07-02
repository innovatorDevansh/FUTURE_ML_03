import re
import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


class SkillExtractor:

    def __init__(self, skills_file: str):

        df = pd.read_csv(skills_file)

        # Store skill list
        self.skills = (
            df["skill"]
            .dropna()
            .str.lower()
            .unique()
            .tolist()
        )

        # Dictionary: skill -> category
        self.skill_category = dict(
            zip(
                df["skill"].str.lower(),
                df["category"]
            )
        )

    def normalize_text(self, text: str) -> str:
        """
        Normalize common resume variations.
        """

        text = text.lower()

        replacements = {
            "node.js": "nodejs",
            "node js": "nodejs",
            "machine-learning": "machine learning",
            "deep-learning": "deep learning",
            "scikit-learn": "scikit learn",
            "power-bi": "power bi",
            "c sharp": "c#",
            "c plus plus": "c++",
            "asp.net": "asp net",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text

    def extract(self, text: str):

        if not isinstance(text, str):
            return []

        text = self.normalize_text(text)

        found_skills = set()

        for skill in self.skills:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text, flags=re.IGNORECASE):

                found_skills.add(skill)

        return sorted(found_skills)

    def process_dataframe(self, df):

        logger.info("Extracting skills...")

        df["skills"] = df["cleaned_text"].apply(self.extract)

        df["skill_count"] = df["skills"].apply(len)

        return df