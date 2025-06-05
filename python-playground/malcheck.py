"""
Poke: A simple port poker. I mean... scanner.
"""

# Created by: Rick Henderson
# Created on: June 4, 2025

import argparse
from colorama import just_fix_windows_console
from colorama import Fore
from colorama import Style

import sys

just_fix_windows_console()


# Re-use code from previous project but modify it.
def write_file(file_name: str, msg: str) -> int:
    """Write test to a file."""
    with open(f"{file_name}", "wt", encoding="utf-8") as out_file:
        out_file.write(f"{msg}\n")
    return 1


def read_file(file_name: str) -> str:
    """Read from the file."""
    try:
        with open(f"{file_name}", "r", encoding="utf-8") as in_file:
            dummy = (
                in_file.readlines()
            )  # Reads the whole file unless the project requires otherwise.
            if dummy:

                return dummy[
                    -1
                ].strip()  # returns the score from the last line, with no newline.
    except FileNotFoundError as e:
        print("Poke: Eek! Couldn't read file! I'll have to quit.")
        return -1
    return 1


def perform_dump():
    """Dump the first 256 bytes of the file in hex."""


def print_banner():
    """Print the banner."""
    color = Fore.GREEN
    banner = """

    ▪  .▄▄ ·     ▪  ▄▄▄▄▄    • ▌ ▄ ·.  ▄▄▄· ▄▄▌  ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ▄▄▄ . ██████╗ 
    ██ ▐█ ▀.     ██ •██      ·██ ▐███▪▐█ ▀█ ██•  ██· █▌▐█▐█ ▀█ ▀▄ █·▀▄.▀· ╚════██╗
    ▐█·▄▀▀▀█▄    ▐█· ▐█.▪    ▐█ ▌▐▌▐█·▄█▀▀█ ██▪  ██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐▀▀▪▄   ▄███╔╝
    ▐█▌▐█▄▪▐█    ▐█▌ ▐█▌·    ██ ██▌▐█▌▐█ ▪▐▌▐█▌▐▌▐█▌██▐█▌▐█ ▪▐▌▐█•█▌▐█▄▄▌   ▀▀══╝ 
    ▀▀▀ ▀▀▀▀     ▀▀▀ ▀▀▀     ▀▀  █▪▀▀▀ ▀  ▀ .▀▀▀  ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀ ▀▀▀    ██╗
                                                                            ╚═╝ 
    """
    print(f"{color}{banner}{Style.RESET_ALL}")


def main(args):
    """Create a binary analysis tool."""

    print_banner()

    print("\n[!] Note: Nothing, we're good.")

    if args.dump:
        print("Dumping file.")
        perform_dump()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="malcheck")
    parser.add_argument("-d", "--dump", help="Dump the first 256 bytes.")
    # Use action="store_true" for flags
    parser.add_argument(
        "-ap",
        "--arping",
        action="store_true",
        help="Perform Scapy arping (accepts CIDR)",
    )
    parser.add_argument(
        "-s", "--synscan", action="store_true", help="Send TCP SYN on ports 1 to 1024."
    )
    args = parser.parse_args()
    print(args)
    # Start the main program and pass in the arguments from the command line.
    main(args)
