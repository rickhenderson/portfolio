"""
Poke: A simple port poker. I mean... scanner.
"""

# Created by: Rick Henderson
# Created on: June 4, 2025

import argparse
import sys
from scapy.all import IP, ls, Ether, sr1, UDP, DNS, arping

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

def perform_arping(targets):
    """Perform the Scapy arping function to determine which hosts are up using `who-has`."""
    try:
        arping(targets)
    except ValueError as e:
        print(f"[!] Could not perform arping. Is the destination address correct? {e}")


def main(args):
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
        "\n[!] Note: Currently only supports scanning one host. Does not accept CIDR notation or domain names."
    )

    target_host = args.arping
    if not target_host:
        print("[!] Can't scan for ports with out a host. Use port.py -t 192.168.1.5.")
        sys.exit
    else:
        print(f"[+] Target host: {target_host}")

    # From https://scapy.readthedocs.io/en/latest/introduction.html#quick-demo

    if args.arping:
        perform_arping(target_host)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="The IP address of the target host.")
    parser.add_argument("-ap", "--arping", help="Perform Scapy arping (accepts CIDR)")
    args = parser.parse_args()
    print(args)

    # Start the main program and pass in the target IP from the command line.
    main(args)
