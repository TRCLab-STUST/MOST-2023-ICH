import time
from typing import Optional


class STime(object):
    __TIME_FORMATE = "%Y%m%d%H%M%S"

    def __init__(self, str_time: Optional[str] = None):
        self.__timestamp = time.time()
        if str_time is not None:
            struct_time = time.strptime(str_time, STime.__TIME_FORMATE)
            self.__timestamp = int(time.mktime(struct_time))

    @property
    def timestamp(self):
        return self.__timestamp

    def __str__(self):
        local_time = time.localtime(self.__timestamp)
        str_time = time.strftime(STime.__TIME_FORMATE, local_time)
        return str_time

    def __sub__(self, other):
        return self.__timestamp - other.timestamp
