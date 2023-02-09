import os

from trclab.datasets.dataset_file_manager import DatasetFileManager


class ICH127FileManager(DatasetFileManager):
    __DATASET_DIR = os.environ["DATASET_ICH_127"]

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

    @property
    def test_image_filepaths(self) -> [str]:
        pass

    @property
    def train_image_filepaths(self) -> [str]:
        pass
