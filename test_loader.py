from src.parser.pdf_reader import ResumeLoader


def main():

    loader = ResumeLoader(
        r"E:\Future\Future_ML_3\data\data\data"
    )

    resumes = loader.load_dataset()

    print("\n")

    print("=" * 80)

    print(f"Total Resumes : {len(resumes)}")

    print("=" * 80)

    for resume in resumes[:5]:

        print(f"\nCategory : {resume['category']}")
        print(f"File     : {resume['filename']}")
        print("-" * 80)
        print(resume["text"][:500])
        print("=" * 80)


if __name__ == "__main__":
    main()