from logging import Logger
from pathlib import Path
from typing import Optional, List

import pandas as pd
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from . import RsnaICHFileManager
from .. import Dataset
from ...ich import ICHType, ICHImage


class DatasetRSNAICH(Dataset):
    def __init__(self, logger: Logger):
        self.__train_labels: Optional[pd.DataFrame] = None
        super().__init__(logger, RsnaICHFileManager(logger.getChild(RsnaICHFileManager.__name__)))
        self.__train_images: Optional[List[ICHImage]] = None

    def prepare_dataset(self):
        """
        資料集取用前期準備

        """
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

    def get_train_set(self):
        # TODO Change to Yield
        if self.__train_images is None:
            self.__train_images = []
            with logging_redirect_tqdm():
                for image_filepath in tqdm(self.dataset_files.train_image_filepaths[:50]):
                    pure_filename = Path(image_filepath).stem
                    row_data = self.__train_labels.loc[self.__train_labels["Image"] == pure_filename]
                    diagnosis_label = ICHType.NOT_ANY
                    for diagnosis in ["INTRAPARENCHYMAL", "INTRAVENTRICULAR", "SUBARACHNOID", "SUBDURAL", "EPIDURAL"]:
                        if row_data[diagnosis.lower()].item():
                            diagnosis_label |= ICHType[diagnosis]

                    ich_image = ICHImage(image_filepath)
                    ich_image.ich_types = diagnosis_label
                    self.__train_images.append(ich_image)

        return self.__train_images

    def get_test_set(self):
        pass
