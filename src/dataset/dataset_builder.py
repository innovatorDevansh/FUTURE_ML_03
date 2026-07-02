"""
Dataset Builder

Creates a structured dataset from all resumes
and stores it in cache/resumes.csv.
"""

from pathlib import Path

import pandas as pd

from src.parser.pdf_reader import ResumeLoader
from src.utils.logger import get_logger

logger = get_logger(__name__)


class DatasetBuilder:

    def __init__(
        self,
        dataset_path: str,
        cache_path: str = "cache/resumes.csv"
    ):

        self.dataset_path = Path(dataset_path)
        self.cache_path = Path(cache_path)

    def build(self) -> pd.DataFrame:
        """
        Build dataset from PDF resumes.
        """

        logger.info("Building dataset from resumes...")

        loader = ResumeLoader(str(self.dataset_path))

        resumes = loader.load_dataset()

        df = pd.DataFrame(resumes)

        self.cache_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_csv(
            self.cache_path,
            index=False,
            encoding="utf-8"
        )

        logger.info(
            f"Dataset cached at {self.cache_path}"
        )

        return df

    def load(self) -> pd.DataFrame:
        """
        Load cached dataset if available.
        """

        if self.cache_path.exists():

            logger.info("Loading cached dataset...")

            return pd.read_csv(self.cache_path)

        return self.build()