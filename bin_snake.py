#!/usr/bin/env python3
"""Program to work with the bin-snake language"""

from argparse import ArgumentParser


def bs_to_py(text: str, should_execute: bool = False) -> str:
    """
    Convert a bin-snake language string to a python language string.
    Optionally runs the code.
    """
    byte = ""
    output = ""
    for i in filter(lambda x: x in "01", text):
        byte += i
        if len(byte) == 8:
            output += chr(int(byte, 2))
            byte = ""
    if should_execute:
        exec(output, {})  # pylint: disable=exec-used
    return output


def get_args() -> ArgumentParser:
    """Handle command line arguments for bin_snake.py"""
    parser = ArgumentParser(description="Bin-snake executable", add_help=False)
    parser.add_argument(
        "--help", "-h", action="help", help="show this help message and exit"
    )
    parser.add_argument("--compile", "-c", help="compile a .bs file to a .py file")
    parser.add_argument("--run", "-r", help="compile and run a .bs file")
    parser.add_argument(
        "--interpret", "-i", help="interpret a .bs string and print the output"
    )
    parser.add_argument("--write", "-w", help="convert a .py file to a .bs file")
    return parser


def _handle_compilation(bs_filename: str) -> None:
    if not bs_filename.endswith(".bs"):
        raise TypeError("File must be a .bs file")
    py_filename = f"{bs_filename[:-3]}.py"
    with open(
        bs_filename,
        "r",
        encoding="utf-8",
    ) as from_, open(
        py_filename,
        "w",
        encoding="utf-8",
    ) as to:
        to.write(bs_to_py(from_.read()))
    print(f"Created: {py_filename}")


def _handle_running(bs_filename: str) -> None:
    if not bs_filename.endswith(".bs"):
        raise TypeError("File must be a .bs file")
    with open(bs_filename, encoding="utf-8") as file:
        bs_to_py(file.read(), True)


def _handle_interpretation(bs_string: str) -> None:
    for char in bs_string:
        if char not in "01":
            print("This isn't bs!")
            return
    bs_to_py(bs_string, True)


def _handle_writing(py_filename: str) -> None:
    if not py_filename.endswith(".py"):
        raise TypeError("File must be a .py file")
    bs_filename = f"{py_filename[:-3]}.bs"
    with open(
        py_filename,
        "r",
        encoding="utf-8",
    ) as from_, open(
        bs_filename,
        "w",
        encoding="utf-8",
    ) as to:
        to.write("".join(bin(ord(i))[2:].zfill(8) for i in from_.read()))
    print(f"Created: {bs_filename}")


def main() -> None:
    """Entry point for bin_snake.py"""
    parser = get_args()
    args = parser.parse_args()
    if args.compile:
        return _handle_compilation(args.compile)
    if args.run:
        return _handle_running(args.run)
    if args.interpret:
        return _handle_interpretation(args.interpret)
    if args.write:
        return _handle_writing(args.write)
    return parser.print_help()


if __name__ == "__main__":
    main()
