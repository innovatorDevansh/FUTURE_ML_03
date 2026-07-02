from pathlib import Path

from src.preprocessing.cleaner import TextCleaner
from src.extraction.skill_extractor import SkillExtractor
from src.utils.logger import get_logger

logger = get_logger(__name__)


class JobDescriptionParser:

    def __init__(self, skills_file: str):

        self.extractor = SkillExtractor(skills_file)

    def read_file(self, file_path: str) -> str:
        """
        Read Job Description text file.
        """

        path = Path(file_path)

        if not path.exists():

            raise FileNotFoundError(f"{file_path} not found.")

        return path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    def parse(self, file_path: str):

        logger.info("Reading Job Description...")

        text = self.read_file(file_path)

        cleaned_text = TextCleaner.clean(text)

        skills = self.extractor.extract(cleaned_text)

        return {
            "job_description": text,
            "cleaned_text": cleaned_text,
            "skills": skills,
            "skill_count": len(skills)
        }