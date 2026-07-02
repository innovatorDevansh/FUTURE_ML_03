from pathlib import Path

from src.parser.pdf_reader import ResumeReader


def main():

    resume_folder = Path("data/resumes")

    reader = ResumeReader()

    resumes = reader.load_resumes(resume_folder)

    print("\n")

    print("=" * 80)

    print(f"Total Resumes Loaded : {len(resumes)}")

    print("=" * 80)

    for resume in resumes:

        print()

        print(f"Resume : {resume['filename']}")

        print("-" * 80)

        print(resume["text"][:800])

        print()

        print("=" * 80)


if __name__ == "__main__":
    main()