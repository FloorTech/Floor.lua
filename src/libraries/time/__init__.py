import time
from libraries.base import BaseLib


class TimeLib(BaseLib):
    @staticmethod
    def __get_access_name__() -> str:
        return "time"

    @staticmethod
    def sleep(seconds: float) -> None:
        time.sleep(seconds)

    @staticmethod
    def now() -> float:
        return time.time()
