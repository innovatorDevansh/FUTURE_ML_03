from src.parser.job_description_parser import JobDescriptionParser


def main():

    parser = JobDescriptionParser(
        "data/skills.csv"
    )

    jd = parser.parse(
        "data/job_descriptions/python_developer.txt"
    )

    print()

    print("=" * 80)

    print("Job Description Skills")

    print("=" * 80)

    for skill in jd["skills"]:

        print(skill)

    print()

    print("=" * 80)

    print("Total Skills :", jd["skill_count"])

    print("=" * 80)


if __name__ == "__main__":
    main()