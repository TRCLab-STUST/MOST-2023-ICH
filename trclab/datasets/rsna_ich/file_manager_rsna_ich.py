import os
import glob
from logging import Logger
from typing import List

from .. import DatasetFileManager


class RsnaICHFileManager(DatasetFileManager):
    __DATASET_DIR = os.environ["DATASET_RSNA_ICH_DIRNAME"]

    def __init__(self, logger: Logger):
        super().__init__(RsnaICHFileManager.__DATASET_DIR, logger)
        self.__dataset_train = os.path.join(self.folder_path, "stage_2_train")
        self.__dataset_test = os.path.join(self.folder_path, "stage_2_train")

    @property
    def train_image_filepaths(self) -> List[str]:
        """
        獲取 RSNA 資料集的訓練集檔案集路徑

        :return: RSNA訓練集檔案路徑
        """
        return glob.glob(os.path.join(self.__dataset_train, "*.dcm"))

    @property
    def test_image_filepaths(self) -> List[str]:
        """
        獲取 RSNA 資料集的測試集檔案集路徑

        :return: RSNA測試集檔案路徑
        """
        return glob.glob(os.path.join(self.__dataset_test, "*.dcm"))

    @property
    def train_label_filepaths(self) -> str:
        """
        獲取 RSNA ICH 影像腦出血類行的標記資料

        :rtype: object
        :return: RSNA ICH 出血類型標記資料
        """
        return os.path.join(self.folder_path, "stage_2_train.csv")

    @property
    def test_label_filepaths(self) -> None:
        """
        RSNA ICH 沒有測試標記

        :rtype: None
        :return: None
        """
        raise FileNotFoundError("RSNA ICH 資料集沒有測試標記檔案")
