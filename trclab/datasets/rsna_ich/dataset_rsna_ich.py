from logging import Logger
from typing import Optional

import pandas as pd

from .. import Dataset
from . import RsnaICHFileManager


class DatasetRSNAICH(Dataset):
    def __init__(self, logger: Logger):
        super().__init__(logger, RsnaICHFileManager(logger.getChild(RsnaICHFileManager.__name__)))
        self.train_labels: Optional[pd.DataFrame] = None

    def prepare_dataset(self):
        """
        資料集取用前期準備

        """
        self.logger.info("Process RSNA Dataset Label CSV.")
        rsna_df = pd.read_csv(self.dataset_files.train_label_filepaths)
        rsna_df[["ID", "Image", "Diagnosis"]] = rsna_df["ID"].str.split("_", expand=True)
        rsna_df = rsna_df[["Image", "Diagnosis", "Label"]]
        rsna_df.drop_duplicates(inplace=True)

        rsna_df = rsna_df.pivot(index="Image",
                                columns="Diagnosis",
                                values="Label").reset_index()
        rsna_df["Image"] = "ID_" + rsna_df["Image"]
        self.train_labels = rsna_df
        self.logger.info("RSNA Dataset Label CSV. Processed Done")
        self.logger.info(rsna_df.head())

        for idx in self.train_labels.index[:10]:
            row_data = self.train_labels.loc[idx]
            for diagnosis in ["INTRAPARENCHYMAL", "INTRAVENTRICULAR", "SUBARACHNOID",
                              "SUBDURAL", "EPIDURAL"]:
                self.logger.info(row_data["intraventricular"])
            # file_basename = f"{row_data['Image']}.dcm"


    def get_train_set(self):
        pass

    def get_test_set(self):
        pass
