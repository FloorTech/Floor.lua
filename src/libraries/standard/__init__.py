from typing import Any
import colorama
from libraries.base import BaseLib


class StandardLib(BaseLib):
    @staticmethod
    def __get_access_name__() -> str:
        return "std"

    @staticmethod
    def debug(text: Any) -> None:
        text = str(text)
        print(text)

    @staticmethod
    def warn(text: Any) -> None:
        text = str(text)
        text = colorama.Fore.YELLOW + text + colorama.Fore.RESET
        print(text)

    @staticmethod
    def error(text: Any) -> None:
        text = str(text)
        text = colorama.Fore.RED + text + colorama.Fore.RESET
        print(text)
