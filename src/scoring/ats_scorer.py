"""
ATS Scoring Engine

Combines Skill Score and Cosine Similarity
to produce the final ATS score.
"""

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


class ATSScorer:

    def __init__(
        self,
        skill_weight: float = 0.70,
        cosine_weight: float = 0.30,
    ):

        self.skill_weight = skill_weight
        self.cosine_weight = cosine_weight

    def get_recommendation(
        self,
        score: float
    ) -> str:

        if score >= 90:
            return "Highly Recommended"

        elif score >= 80:
            return "Recommended"

        elif score >= 70:
            return "Consider"

        elif score >= 60:
            return "Needs Review"

        return "Not Recommended"

    def score_dataframe(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info("Calculating ATS Score...")

        df["ats_score"] = (
            (
                df["skill_score"] * self.skill_weight
            )
            +
            (
                df["cosine_score"] * self.cosine_weight
            )
        ).round(2)

        logger.info("Ranking candidates...")

        df = df.sort_values(
            by="ats_score",
            ascending=False
        ).reset_index(drop=True)

        df["rank"] = (
            df.index + 1
        )

        df["recommendation"] = (
            df["ats_score"]
            .apply(self.get_recommendation)
        )

        return df