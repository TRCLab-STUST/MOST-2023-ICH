import os
import abc
import logging

from trclab.datasets import DatasetType, DatasetManager
from trclab.datasets import DatasetICH420, DatasetRSNAICH


class TRCLabApp(abc.ABC):
    RUNTIME_TYPE = os.environ["PROJECT_RUNTIME"]

    __LOGGER: logging.Logger = logging.getLogger(name="TRCLabApp")
    __HANDLER: logging.StreamHandler = logging.StreamHandler()
    __FORMATTER: logging.Formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(name)s] %(message)s")

    __LOGGER.setLevel(logging.DEBUG)
    __HANDLER.setFormatter(__FORMATTER)
    __LOGGER.addHandler(__HANDLER)

    def __init__(self, app_name: str):
        self.__app_name = app_name
        self.__logger = TRCLabApp.__LOGGER.getChild(self.__app_name)
        self.__dataset_manager = DatasetManager(
            TRCLabApp.__LOGGER.getChild("dataset_manager")
        )

    @property
    def logger(self) -> logging.Logger:
        """
        Get TRCLab Application Recorder.

        :return: App Logger
        """
        return self.__logger

    @property
    def app_name(self) -> str:
        """
        Get App name

        :return: App Name
        """
        return self.__app_name

    @property
    def datasets(self) -> DatasetManager:
        """
        取的資料集管理器

        :return: 資料集管理器
        """
        return self.__dataset_manager

    def __launch(self) -> None:
        """
        Do something when the application is launched

        """
        self.on_enable()  # must be the last line

    def __stop(self) -> None:
        """
        Do something when the application is stopped

        """
        self.on_disable()  # must be the first line

    def run(self) -> None:
        """
        Start your application.

        """
        # Register Dataset
        self.__dataset_manager.register(DatasetType.ICH_420, DatasetICH420)
        self.__dataset_manager.register(DatasetType.RSNA_ICH, DatasetRSNAICH)

        TRCLabApp.__LOGGER.info("TRCLab application framework launched.")
        self.__launch()  # must be the last line

    def __del__(self):
        """
        Run when a class instance is destructured

        """
        self.__stop()  # must be the last line
        TRCLabApp.__LOGGER.info("TRCLab application framework stopped.")

    @abc.abstractmethod
    def on_enable(self) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def on_disable(self) -> None:
        raise NotImplemented
