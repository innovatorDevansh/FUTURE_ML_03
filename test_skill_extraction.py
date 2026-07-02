import pandas as pd

from src.extraction.skill_extractor import SkillExtractor


def main():

    df = pd.read_csv("cache/resumes_cleaned.csv")

    extractor = SkillExtractor(
        "data/skills.csv"
    )

    df = extractor.process_dataframe(df)

    df.to_csv(
        "cache/resumes_skills.csv",
        index=False
    )

    print()

    print("=" * 80)

    print(
        df[
            [
                "category",
                "skills",
                "skill_count"
            ]
        ].head(10)
    )

    print()

    print("=" * 80)

    print("Saved -> cache/resumes_skills.csv")


if __name__ == "__main__":
    main()