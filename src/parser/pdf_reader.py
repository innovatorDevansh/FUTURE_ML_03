"""
Resume PDF Loader

Reads PDF resumes stored in category-wise folders.

Example:

data/
│
├── Accountant/
│     resume1.pdf
│     resume2.pdf
│
├── HR/
│     hr1.pdf
│
├── Java Developer/
│     java1.pdf
"""

from pathlib import Path
from typing import List, Dict

import pdfplumber

from src.utils.logger import get_logger

logger = get_logger(__name__)


class ResumeLoader:
    """
    Loads resume PDFs from nested folders.
    """

    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)

    def extract_text(self, pdf_path: Path) -> str:
        """
        Extract text from a PDF.
        """

        text = ""

        try:
            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

        except Exception as e:

            logger.error(f"Error reading {pdf_path.name}")

            logger.error(e)

        return text.strip()

    def load_dataset(self) -> List[Dict]:
        """
        Loads every PDF from every category folder.

        Returns
        -------
        List[Dict]
        """

        resumes = []

        if not self.dataset_path.exists():

            logger.error("Dataset folder not found.")

            return resumes

        category_count = 0

        resume_count = 0

        for category_folder in sorted(self.dataset_path.iterdir()):

            if not category_folder.is_dir():
                continue

            category = category_folder.name

            category_count += 1

            pdf_files = list(category_folder.glob("*.pdf"))

            logger.info(
                f"{category} -> {len(pdf_files)} resumes"
            )

            for pdf in pdf_files:

                resume_count += 1

                text = self.extract_text(pdf)

                resumes.append(
                    {
                        "filename": pdf.name,
                        "category": category,
                        "filepath": str(pdf),
                        "text": text,
                    }
                )

        logger.info("=" * 60)
        logger.info(f"Categories : {category_count}")
        logger.info(f"Total PDFs : {resume_count}")
        logger.info("=" * 60)

        return resumes