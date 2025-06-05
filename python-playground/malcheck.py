"""
Malcheck - A simple binary analysis tool.
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

def isPE(buffer):
    """Use the provided byte buffer to determine if the file is a PE file."""
    if buffer[0:2] == b"MZ":
        return True

def perform_checks(file_bytes):
    print(f"\nPE file: {isPE(file_bytes[0:2])}")


def perform_dump(file_to_dump:str)->str:
    """Dump the first 256 bytes of the file in hex."""
    try:
        with open(file_to_dump, "rb") as bytes:
            result = bytes.read(256)
            print(result)
    except FileNotFoundError as e:
        print(e)
        sys.exit(-1)

    return result

    
    

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

    if args.dump:
        file_as_bytes = perform_dump(args.dump)

    perform_checks(file_as_bytes)




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
