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
    for char in plaintext:
        ciphertext += chr((ord(char)+13) % 94)
    return ciphertext

def reverse(plaintext :str) -> str:
    return plaintext[::-1]


def main():
    print("[+] Enter '-1' to quit.")
    plaintext = ""
    while plaintext != "-1":
        plaintext = input("Enter a plain text message: ")
        if plaintext != "-1":
            print(f"{Fore.CYAN}[+] The ciphertext is {convert(plaintext)}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}[+] ROT13: {rot13(plaintext)}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}[+] Reverse: {reverse(plaintext)}{Style.RESET_ALL}")
           
    
if __name__ == "__main__":
    print(f"{Fore.MAGENTA}++ Assumption: plaintext messages are composed of printable ASCII characters including the upper and lower case English alphabet, numbers from 0-1, and common punctuation.")
    print("[+] This is the set of printable ASCII characters from chr(32) to chr(126).")
    print(f"{Style.RESET_ALL}")

    main()

    print("\n Thank you for your time. :)\n")