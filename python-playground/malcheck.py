"""
Malcheck - A simple binary analysis tool.
"""

# Created by: Rick Henderson
# Created on: June 4, 2025

import argparse
from colorama import just_fix_windows_console
from colorama import Fore
from colorama import Style

import hashlib
import json
import os
import requests
import sys

just_fix_windows_console()

# Set a global debug flag for certain output required to help debug the program.
DEBUG = True

# Re-use code from previous project but modify it.
def write_text_file(file_name: str, msg: str) -> int:
    """Write test to a file."""
    with open(f"{file_name}", "wt", encoding="utf-8") as out_file:
        out_file.write(f"{msg}\n")
    return 1


def read_text_file(file_name: str) -> str:
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

def perform_checks(file_name):
    """Perform checks against the file."""
    file_size = os.path.getsize(file_name)
    print(f"\nFile size: {file_size:,} bytes")
    print(os.stat(file_name))


def perform_dump(file_to_dump:str)->str:
    """Dump the first 256 bytes of the file in hex."""
    try:
        with open(file_to_dump, "rb") as bytes:
            result = bytes.read(256)
            print(f"\nPE file: {isPE(result[0:2])}")

    except FileNotFoundError as e:
        print(e)
        sys.exit(-1)

    return result

def get_full_file_as_bytes(file_to_get:str)->bytes:
    with open(file_to_get, "+rb") as f:
        # Read the entire file into a byte array.
        file_bytes = f.read()
    return file_bytes    

def print_banner():
    """Print the banner."""
    color = Fore.GREEN
    banner = """

    ▪  .▄▄ ·     ▪  ▄▄▄▄▄    • ▌ ▄ ·.  ▄▄▄· ▄▄▌  ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ▄▄▄ . ██████╗ 
    ██ ▐█ ▀.     ██ •██      ·██ ▐███▪▐█ ▀█ ██•  ██· █▌▐█▐█ ▀█ ▀▄ █·▀▄.▀· ╚════██╗
    ▐█·▄▀▀▀█▄    ▐█· ▐█.▪    ▐█ ▌▐▌▐█·▄█▀▀█ ██▪  ██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐▀▀ ▄   ▄███╔╝
    ▐█▌▐█▄▪▐█    ▐█▌ ▐█▌·    ██ ██▌▐█▌▐█ ▪▐▌▐█▌▐▌▐█▌██▐█▌▐█ ▪▐▌▐█•█▌▐█▄▄▌   ▀▀══╝ 
    ▀▀▀ ▀▀▀▀     ▀▀▀ ▀▀▀     ▀▀  █▪▀▀▀ ▀  ▀ .▀▀▀  ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀ ▀▀▀    ██╗
                                                                            ╚═╝ 
    """
    print(f"{color}{banner}{Style.RESET_ALL}")

def get_SHA256(file_name):
    sample_file = get_full_file_as_bytes(file_name)
    sha256 = hashlib.sha256(sample_file).hexdigest()
    return sha256

def get_virustotal_info(file_hash:str):
    print("[+] Requesting malware search from VirusTotal...")
    file_report_endpoint = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"accept": "application/json",
               "X-Apikey": f"{args.vtapi}"}
    
    try:
        vt_file_report = requests.get(file_report_endpoint, headers=headers)
    except TimeoutError as e:
        print("[!] There was a problem getting a response from VirusTotal. Try again later or check your API key.")
    return vt_file_report


def main(args):
    """Create a binary analysis tool."""

    print_banner()


    # Perform the options requested by the user from the command line
    if args.dump:
        file_as_bytes = perform_dump(args.file)
        print(file_as_bytes)

    if args.hash:
        sha256_hash = get_SHA256(args.file)
        print(f"\nSHA256: {sha256_hash}")

    if args.info:
        perform_checks(args.file)

    if args.vtapi:
        # Returns a Response Object
        black_basta_sample = "1fd90c1d55def54f85d8ebf5b2fdf31e11314af41833c13b73b87e3047879099"
        vt_report = get_virustotal_info(get_SHA256(args.file))
        
        # Step-by-step to make it easuer to figure out in the future
        content = vt_report.content    # Returns a string string in bytes ie. b'{"data": {"id": "ce5d1...
        print()

        # There must be a better way other than this and slicing.
        #fixed = content_as_text.lstrip("b'").rstrip("'")
        
        # Convert the returned string into a Json object
        json_report = json.loads(content.decode('utf-8'))
        print(f"Reputation: {json_report['data']['attributes']['reputation']}")
        print(f"Type Extention: {json_report['data']['attributes']['type_extension']}")
        print(f"Stats: {json_report['data']['attributes']['last_analysis_stats']}")
        print(f"Magic string: {json_report['data']['attributes']['magic']}")
        print(f"Unique Sources: {json_report['data']['attributes']['unique_sources']}")

        # There are many entries for language so a specific one may be required.
        print(f"Resource Language: {json_report['data']['attributes']['pe_info']['resource_details'][0]['lang']}")
        print(f"Likely Compiler: {json_report['data']['attributes']['pe_info']['compiler_product_versions'][0]}")

        # TODO: Nice way to display these
        print(f"Import List: {json_report['data']['attributes']['pe_info']['import_list']}")


        
        
        
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="malcheck")

    # Set up the list of command line options
    parser.add_argument("-f", "--file", help="Name of the file to analyze.")
    parser.add_argument("-i", "--info", action="store_true", help="Display file info.")
    parser.add_argument("-d", "--dump", action="store_true", help="Dump the first 256 bytes.")
    parser.add_argument("-vt", "--vtapi",help="A VirusTotal API key to get a VT report.")
    parser.add_argument("-hash", "--hash", action="store_true", help="Display the SHA256 hash.")

    args = parser.parse_args()
    if DEBUG:
        print(args)

    # Start the main program and pass in the arguments from the command line.
    main(args)
