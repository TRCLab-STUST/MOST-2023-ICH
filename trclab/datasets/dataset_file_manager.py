import os
import abc
from logging import Logger


class DatasetFileManager(abc.ABC):

    def __init__(self, dataset_dir: str = "", logger: Logger = None):
        from trclab.application import TRCLabApp

        self.__folder_path = ""
        self.__logger = logger
        if TRCLabApp.RUNTIME_TYPE == "LOCAL":
            self.__folder_path = os.environ["DATASET_DIR"]
        elif TRCLabApp.RUNTIME_TYPE == "CONTAINER":
            self.__folder_path = os.environ["DOCKER_MOUNT_DATASET_DIR"]
        else:
            raise TypeError

        if dataset_dir == "":
            raise ValueError("請提供資料集的資料夾名稱")

        self.__dataset_dir = os.path.join(self.__folder_path, dataset_dir)

    @property
    def logger(self) -> Logger:
        return self.__logger

    @property
    def folder_path(self) -> str:
        return self.__dataset_dir

    @property
    @abc.abstractmethod
    def train_image_filepaths(self) -> [str]:
        return NotImplemented

    @property
    @abc.abstractmethod
    def test_image_filepaths(self) -> [str]:
        return NotImplemented

    @property
    @abc.abstractmethod
    def train_label_filepaths(self) -> [str]:
        return NotImplemented

    @property
    @abc.abstractmethod
    def test_label_filepaths(self) -> [str]:
        return NotImplemented
