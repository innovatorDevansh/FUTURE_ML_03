import ast
import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


class ResumeMatcher:

    def __init__(self, jd_skills):

        self.jd_skills = set(skill.lower() for skill in jd_skills)

    def match_resume(self, resume_skills):

        if isinstance(resume_skills, str):
            resume_skills = ast.literal_eval(resume_skills)

        resume_skills = set(skill.lower() for skill in resume_skills)

        matched = sorted(resume_skills & self.jd_skills)

        missing = sorted(self.jd_skills - resume_skills)

        extra = sorted(resume_skills - self.jd_skills)

        score = round(
            (len(matched) / len(self.jd_skills)) * 100,
            2
        )

        return {
            "matched_skills": matched,
            "missing_skills": missing,
            "extra_skills": extra,
            "matched_count": len(matched),
            "missing_count": len(missing),
            "skill_score": score
        }

    def process_dataframe(self, df):

        logger.info("Matching resumes with Job Description...")

        results = []

        for _, row in df.iterrows():

            result = self.match_resume(row["skills"])

            results.append(result)

        result_df = pd.DataFrame(results)

        return pd.concat(
            [df, result_df],
            axis=1
        )