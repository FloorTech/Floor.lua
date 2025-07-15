from typing import Any
from libraries.base import BaseLib
from libraries.standard import StandardLib
from libraries.time import TimeLib

type LuaEnvironment = dict[str, Any]


def get_libraries() -> list[type[BaseLib]]:
    return [
        StandardLib,
        TimeLib,
    ]
