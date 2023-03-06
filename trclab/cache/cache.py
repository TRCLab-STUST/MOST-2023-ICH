import glob
import os
import pickle
from logging import Logger
from pathlib import Path
from typing import Optional

from ..time import STime


class Cache(object):
    __CACHE_FOLDER = os.environ["CACHE_FOLDER"]

    def __init__(self, object_name, logger: Logger, expired_time: int = 86400):
        os.makedirs(Cache.__CACHE_FOLDER, exist_ok=True)
        self.__logger = logger.getChild(self.__class__.__name__)
        self.__object_name = object_name
        self.__expired_time = expired_time
        self.__filename = os.path.join(Cache.__CACHE_FOLDER, self.__object_name)
        self.__cache_file = self.__get_cache_file()

        if self.__cache_file is not None:
            self.__logger.info(f"Cache file '{self.__cache_file}' founded.")

    def save(self, data_obj):
        """
        儲存物件快取

        :param data_obj: 需快取物件
        """
        if data_obj is None:
            self.__logger.warning("Cache object can't be 'None'")
            raise ValueError

        with open(f"{self.__filename}_{STime()}.tlab", "wb") as cache_file:
            pickle.dump(data_obj, cache_file)

        self.__cache_file = self.__get_cache_file()

    def load(self):
        """
        載入快取物件

        :return: 載入物件
        """
        if self.__cache_file is None:
            self.__logger.error("Cache file not founded.")
            raise FileNotFoundError

        with open(self.__cache_file, "rb") as cache_file:
            return pickle.load(cache_file)

    def is_exists(self):
        return self.__get_cache_file() is not None

    def __get_cache_file(self) -> Optional[str]:
        cache_list = glob.glob(f"{self.__filename}_*.tlab")
        cache_list.sort()

        if len(cache_list) > 1:
            for cache_filepath in cache_list[:-1]:
                self.__logger.info(f"Remove old cache file '{cache_filepath}'.")
                os.remove(cache_filepath)

        cache_filepath = cache_list[-1]
        filename = Path(cache_filepath).stem
        str_time = filename.split("_")[-1]

        if (STime() - STime(str_time)) >= self.__expired_time:
            self.__logger.info(f"Remove expired cache file '{cache_filepath}'.")
            os.remove(cache_filepath)
            return None

        return cache_filepath
