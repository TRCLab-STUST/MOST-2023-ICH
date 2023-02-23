import abc
from typing import Optional
from logging import Logger

from .dataset_file_manager import DatasetFileManager


class Dataset(abc.ABC):
    def __init__(self, logger: Logger, dataset_file_manager: Optional[DatasetFileManager.__subclasses__] = None):
        self.__logger = logger

        if dataset_file_manager is None:
            self.__logger.error("Dataset file manager not defined.")
            raise ValueError("Dataset file manager not defined.")

        if not isinstance(dataset_file_manager, DatasetFileManager):
            self.__logger.error(f"'{dataset_file_manager.__name__}' must be an instance"
                                f" of class '{DatasetFileManager.__name__}.'")
            raise AttributeError(f"'{dataset_file_manager.__name__}' must be an instance"
                                 f" of class '{DatasetFileManager.__name__}.'")

        self.__dataset_file_manager = dataset_file_manager

    @property
    def dataset_files(self):
        """
        取得資料集檔案

        :return: DatasetFileManager
        """
        return self.__dataset_file_manager

    @abc.abstractmethod
    def get_train_set(self):
        """
        需要實做取的訓練資料集

        """
        raise NotImplemented

    @abc.abstractmethod
    def get_test_set(self):
        """
        需要實做取的測試資料集

        """
        raise NotImplemented
