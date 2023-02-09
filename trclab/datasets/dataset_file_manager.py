import abc


class DatasetFileManager(abc.ABC):
    def __init__(self, dataset_dir: str):
        self.__dataset_dir = dataset_dir

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
