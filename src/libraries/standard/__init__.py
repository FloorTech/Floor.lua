import colorama
from libraries.base import BaseLib


class StandardLib(BaseLib):
    @staticmethod
    def __get_access_name__() -> str:
        return "std"

    @staticmethod
    def debug(text: str) -> None:
        print(text)

    @staticmethod
    def warn(text: str) -> None:
        text = colorama.Fore.YELLOW + text + colorama.Fore.RESET
        print(text)

    @staticmethod
    def error(text: str) -> None:
        text = colorama.Fore.RED + text + colorama.Fore.RESET
        print(text)
