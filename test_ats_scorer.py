import pandas as pd

from src.scoring.ats_scorer import ATSScorer


def main():

    resumes = pd.read_csv(
        "cache/resume_similarity.csv"
    )

    scorer = ATSScorer()

    result = scorer.score_dataframe(
        resumes
    )

    result.to_csv(
        "cache/final_resume_ranking.csv",
        index=False
    )

    print()

    print("=" * 120)

    print(
        result[
            [
                "rank",
                "category",
                "skill_score",
                "cosine_score",
                "ats_score",
                "recommendation"
            ]
        ].head(20)
    )

    print()

    print("=" * 120)

    print(
        "Saved -> cache/final_resume_ranking.csv"
    )


if __name__ == "__main__":
    main()