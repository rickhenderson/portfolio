"""
Poke: A simple port poker. I mean... scanner.
"""

# Created by: Rick Henderson
# Created on: June 4, 2025

import argparse


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


def main(target_host: str):
    """Create a port scanner"""

    banner = """
    
 ██▓███   ▒█████   ██ ▄█▀▓█████      ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒ ██▄█▒ ▓█   ▀    ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓███▄░ ▒███      ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▓██ █▄ ▒▓█  ▄      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░▒██▒ █▄░▒████▒   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░   ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░       ░ ░ ░ ▒  ░ ░░ ░    ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
             ░ ░  ░  ░      ░  ░         ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                            ░                                                        
"""

    print(banner)

    print(
        "\n\n[!] Note: Currently only supports scanning one host. Does not accept CIDR notation."
    )
    print(f"[+] Target host: {target_host}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="The IP address of the target host.")
    args = parser.parse_args()

    # Start the main program and pass in the target IP from the command line.
    main(args.target)
