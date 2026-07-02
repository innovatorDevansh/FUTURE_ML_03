import pandas as pd

from src.parser.job_description_parser import JobDescriptionParser
from src.matching.matcher import ResumeMatcher


def main():

    resumes = pd.read_csv(
        "cache/resumes_skills.csv"
    )

    parser = JobDescriptionParser(
        "data/skills.csv"
    )

    jd = parser.parse(
        "data/job_descriptions/python_developer.txt"
    )

    matcher = ResumeMatcher(
        jd["skills"]
    )

    result = matcher.process_dataframe(
        resumes
    )

    result.to_csv(
        "cache/resume_matching.csv",
        index=False
    )

    print()

    print("=" * 100)

    print(
        result[
            [
                "category",
                "skill_score",
                "matched_count",
                "missing_count"
            ]
        ].head(10)
    )

    print()

    print("=" * 100)

    print("Saved -> cache/resume_matching.csv")


if __name__ == "__main__":
    main()