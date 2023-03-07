import time
from typing import Optional


class STime(object):
    __TIME_FORMATE = "%Y%m%d%H%M%S"

    def __init__(self, str_time: Optional[str] = None):
        """
        STime的建構元，如果傳入字串時間則使用該時間，否則自動取得當前時間

        字串時時間格式為 %Y%m%d%H%M%S, EX. 20230201183000
        """
        self.__timestamp = time.time()
        if str_time is not None:
            struct_time = time.strptime(str_time, STime.__TIME_FORMATE)
            self.__timestamp = int(time.mktime(struct_time))

    @property
    def timestamp(self) -> int:
        """
        取的時間戳記

        :return: int
        """
        return self.__timestamp

    def __str__(self) -> str:
        """
        以文字方式回傳時間

        Ex. 當前時間為 2023/03/07 - 15:19:50
        回傳則為 20230307151950

        :return: 當前時間的字串
        """
        local_time = time.localtime(self.__timestamp)
        str_time = time.strftime(STime.__TIME_FORMATE, local_time)
        return str_time

    def __sub__(self, other) -> float:
        """
        計算時間差

        :param other: STime
        :return: 時間差(秒)
        """
        return self.__timestamp - other.timestamp
