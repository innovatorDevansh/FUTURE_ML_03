from src.dataset.dataset_builder import DatasetBuilder


def main():

    builder = DatasetBuilder(
        dataset_path=r"E:\Future\Future_ML_3\data\data\data"
    )

    df = builder.load()

    print()

    print("=" * 80)
    print("DATASET INFORMATION")
    print("=" * 80)

    print(df.head())

    print()

    print("=" * 80)

    print(f"Total Resumes   : {len(df)}")
    print(f"Total Categories: {df['category'].nunique()}")

    print("=" * 80)

    print()

    print(df["category"].value_counts())

    print()

    print("=" * 80)

    print(df.info())


if __name__ == "__main__":
    main()