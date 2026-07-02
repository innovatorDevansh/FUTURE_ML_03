from pathlib import Path

import pandas as pd

from src.preprocessing.preprocessor import ResumePreprocessor


def main():

    df = pd.read_csv("cache/resumes.csv")

    processor = ResumePreprocessor()

    df = processor.process_dataframe(df)

    Path("cache").mkdir(exist_ok=True)

    df.to_csv(
        "cache/resumes_cleaned.csv",
        index=False
    )

    print()

    print("=" * 80)

    print(df[["category", "cleaned_text"]].head())

    print()

    print("=" * 80)

    print("Saved to cache/resumes_cleaned.csv")


if __name__ == "__main__":
    main()