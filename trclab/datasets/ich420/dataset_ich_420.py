from logging import Logger

from .. import Dataset
from . import ICH420FileManager


class DatasetICH420(Dataset):

    def __init__(self, logger: Logger):
        super().__init__(logger, ICH420FileManager)

    def get_test_set(self):
        pass

    def get_train_set(self):
        pass
