import pandas as pd

from src.ml.similarity import ResumeSimilarity
from src.parser.job_description_parser import JobDescriptionParser


def main():

    print("=" * 100)
    print("Loading Resume Dataset")
    print("=" * 100)

    resumes = pd.read_csv(
        "cache/resume_matching.csv"
    )

    parser = JobDescriptionParser(
        "data/skills.csv"
    )

    jd = parser.parse(
        "data/job_descriptions/python_developer.txt"
    )

    similarity = ResumeSimilarity()

    resumes = similarity.process_dataframe(
        resumes,
        jd["cleaned_text"]
    )

    resumes.to_csv(
        "cache/resume_similarity.csv",
        index=False
    )

    print()

    print("=" * 100)

    print(
        resumes[
            [
                "category",
                "skill_score",
                "cosine_score"
            ]
        ].head(15)
    )

    print()

    print("=" * 100)

    print(
        "Dataset saved to cache/resume_similarity.csv"
    )

    print("=" * 100)


if __name__ == "__main__":
    main()