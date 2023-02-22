import os

from .. import DatasetFileManager


class ICH2500FileManager(DatasetFileManager):
    __DATASET_DIR = os.environ["DATASET_ICH_2500_DIRNAME"]

    @property
    def test_image_filepaths(self) -> [str]:
        # TODO Get train image filepaths
        pass

    @property
    def train_image_filepaths(self) -> [str]:
        # TODO Get train image filepaths
        pass

    @property
    def train_label_filepaths(self) -> [str]:
        # TODO Get train label filepaths
        pass

    @property
    def test_label_filepaths(self) -> [str]:
        # TODO Get test label filepaths
        pass
