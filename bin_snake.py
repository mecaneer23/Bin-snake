#!/usr/bin/env python3

import argparse


def compile(text, run=False):
    byte = ""
    output = ""
    for i in text:
        if i in ("0", "1"):
            byte += i
            if len(byte) == 8:
                output += chr(int(byte, 2))
                byte = ""
    if run:
        exec(output)
    return output


def add_zero(binary):
    if len(binary) < 8:
        return add_zero(f"0{binary}")
    return binary


def main():
    parser = argparse.ArgumentParser(description="Bin-snake executable", add_help=False)
    parser.add_argument(
        "--help", "-h", action="help", help="show this help message and exit"
    )
    parser.add_argument("--compile", "-c", help="compile a .bs file to a .py file")
    parser.add_argument("--run", "-r", help="compile and run a .bs file")
    parser.add_argument(
        "--interpret", "-i", help="interpret a .bs string and print the output"
    )
    parser.add_argument("--write", "-w", help="convert a .py file to a .bs file")
    args = parser.parse_args()

    if args.compile:
        if not args.compile.endswith(".bs"):
            return "File must be a .bs file"
        with open(args.compile, "r") as f:
            with open(f"{args.compile[:-3]}.py", "w") as g:
                g.write(compile(f.read()))
        print(f"Created: {args.compile[:-3]}.py")
    elif args.run:
        if not args.run.endswith(".bs"):
            return "File must be a .bs file"
        with open(args.run) as f:
            compile(f.read(), True)
    elif args.interpret:
        for i in args.interpret:
            if i not in ("0", "1"):
                print("This isn't bs!")
                exit()
        compile(args.interpret, True)
    elif args.write:
        if not args.write.endswith(".py"):
            return "File must be a .py file"
        with open(args.write, "r") as f:
            with open(f"{args.write[:-3]}.bs", "w") as g:
                g.write("".join(add_zero(bin(ord(i))[2:]) for i in f.read()))
        print(f"Created: {args.write[:-3]}.bs")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
