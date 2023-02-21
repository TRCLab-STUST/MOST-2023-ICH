import abc
from typing import Optional
from logging import Logger

from . import DatasetFileManager


class Dataset(abc.ABC):
    def __init__(self, logger: Logger, dataset_file_manager: Optional[DatasetFileManager.__subclasses__] = None):
        self.__logger = logger

        if dataset_file_manager is None:
            self.__logger.error("Dataset file manager not defined.")
            raise ValueError("Dataset file manager not defined.")

        # Check is subclass
        if not issubclass(dataset_file_manager, DatasetFileManager):
            self.__logger.error(
                f"Dataset class '{dataset_file_manager.__name__}' must inherit class '{DatasetFileManager.__name__}'")
            raise TypeError(f"'{dataset_file_manager.__name__}' must inherit class '{DatasetFileManager.__name__}'")

        self.__dataset_file_manager = dataset_file_manager

    @abc.abstractmethod
    def get_train_set(self):
        return NotImplemented

    @abc.abstractmethod
    def get_test_set(self):
        return NotImplemented
