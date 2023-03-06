from pathlib import Path
from logging import Logger
from typing import Optional, Generator

import pandas as pd

from .. import Dataset
from . import RsnaICHFileManager
from ...ich import ICHType, ICHImage
from ...cache import Cache


class DatasetRSNAICH(Dataset):
    def __init__(self, logger: Logger):
        self.__train_labels: Optional[pd.DataFrame] = None
        super().__init__(logger, RsnaICHFileManager(logger.getChild(RsnaICHFileManager.__name__)))

    def prepare_dataset(self):
        """
        資料集取用前期準備

        先尋找是否有可用的快取資料，如果沒有則生成資料並快取起來。

        """
        # Check Cache
        train_label_cache = Cache(f"{self.__class__.__name__}-train-label", self.logger)
        self.__train_labels = train_label_cache.load()

        # if data is none
        if self.__train_labels is None:
            self.logger.info("Process RSNA Dataset Label CSV.")
            rsna_df = pd.read_csv(self.dataset_files.train_label_filepaths)
            rsna_df[["ID", "Image", "Diagnosis"]] = rsna_df["ID"].str.split("_", expand=True)
            rsna_df = rsna_df[["Image", "Diagnosis", "Label"]]
            rsna_df.drop_duplicates(inplace=True)
            rsna_df = rsna_df.pivot(index="Image",
                                    columns="Diagnosis",
                                    values="Label").reset_index()
            rsna_df["Image"] = "ID_" + rsna_df["Image"]

            self.__train_labels = rsna_df
            self.logger.info("RSNA Dataset Label CSV. Processed Done")

            # 儲存快取資料
            train_label_cache.save(rsna_df)
            self.logger.info("Create Label CSV Cache file.")

    def get_train_set(self) -> Generator[ICHImage, None, None]:
        for image_filepath in self.dataset_files.train_image_filepaths:
            pure_filename = Path(image_filepath).stem
            row_data = self.__train_labels.loc[self.__train_labels["Image"] == pure_filename]
            diagnosis_label = ICHType.NOT_ANY
            for diagnosis in ["INTRAPARENCHYMAL", "INTRAVENTRICULAR", "SUBARACHNOID", "SUBDURAL", "EPIDURAL"]:
                if row_data[diagnosis.lower()].item():
                    diagnosis_label |= ICHType[diagnosis]

            ich_image = ICHImage(image_filepath)
            ich_image.ich_types = diagnosis_label

            yield ich_image

    def get_test_set(self):
        pass
