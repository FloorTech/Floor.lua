from typing import Any
import sys
import os
from lupa import LuaRuntime
from libraries.base import BaseLib
from libraries.standard import StandardLib


def wrap_library_methods(library: type[BaseLib]) -> dict[str, Any]:
    return {
        name: getattr(library, name)
        for name in dir(library)
        if callable(getattr(library, name)) and not name.startswith("_")
    }


def create_code_runner():
    lua = LuaRuntime()
    safe_env = lua.eval("{}")
    safe_env["math"] = lua.eval("math")  # type: ignore
    safe_env["string"] = lua.eval("string")  # type: ignore

    safe_env[StandardLib.__get_access_name__()] = wrap_library_methods(StandardLib)  # type: ignore

    def run_lua(code: str):  # type: ignore
        try:
            return lua.eval(
                "function(code, env) return assert(load(code, nil, 't', env))() end"
            )(code, safe_env)  # type: ignore
        except Exception as e:
            print(f"Could not execute code! {e}")
            return None

    return run_lua


run_code = create_code_runner()


def main() -> None:
    if not len(sys.argv) > 1:
        print("[=== Floor.lua REPL ===]")
        print("Type 'exit' to exit the REPL.")
        print("")

        def loop():
            while True:
                code = input("> ")

                if code.lower() == "exit":
                    break

                if (
                    not code.startswith("return")
                    and not code.startswith("local")
                    and not code.endswith("end")
                ):
                    code = f"return {code}"

                result = run_code(code)  # type: ignore

                if result is not None:
                    StandardLib.debug(f"Line returned {result}")  # type: ignore

        loop()
        return

    filepath = " ".join(sys.argv[1:])

    if not os.path.exists(filepath):
        StandardLib.error("You must specify a valid Floor.lua file path!")
        return

    if not os.path.isfile(filepath):
        StandardLib.error("You must specify a valid Floor.lua file path!")
        return

    with open(filepath, "r") as f:
        lines = f.readlines()

        for line in lines:
            run_code(line)


if __name__ == "__main__":
    main()
