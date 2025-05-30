# Coding interview practice: write a simple cipher encryption program
# Be able to implment basic ciphers

from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore
from colorama import Style
import re

def convert(msg):
    return "[!] Not yet implemented."

def rot13(plaintext :str):
    ciphertext = ""

    return ciphertext

def main():
    print("[+] Enter '-1' to quit.")
    plaintext = ""
    while plaintext != "-1":
        plaintext = input("Enter a plain text message: ")
        if plaintext != "-1":
            print(f"{Fore.CYAN}[+] The ciphertext is {convert(plaintext)}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}[+] ROT13: {rot13(plaintext)}{Style.RESET_ALL}")

            
    
if __name__ == "__main__":
    main()
