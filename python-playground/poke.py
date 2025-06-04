"""
Poke: A simple port poker. I mean... scanner.
"""

# Created by: Rick Henderson
# Created on: June 4, 2025

import re
import sys


# Re-use code from previous project but modify it.
def write_file(file_name:str, msg:str)->int:
    """Write test to a file."""
    with open(f"{file_name}", "wt", encoding="utf-8") as out_file:
        out_file.write(f"{msg}\n")
    return 1


def read_file(file_name:str)->str:
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
        return None

def main():
    """Create a port scanner"""

if __name__ == "__main__":
    main()
