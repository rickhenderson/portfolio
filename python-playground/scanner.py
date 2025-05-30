#!/usr/bin/env python

from __future__ import print_function

__description__ = 'Port Scanner Using Impacket'
__author__ = 'Rick Henderson'
__version__ = '0.0.1'
__date__ = '2025/05/30'

"""
Source code by Rick Henderson, copyright Rick Henderson.
Use at your own risk.

Resources:
  * https://github.com/fortra/impacket/
  * 
  * https://denizhalil.com/2025/05/02/what-is-impacket-network-toolkit/

History:
  20250530: Start, based on template style from Didier Stevens.

  
Todo:
    * Implement use of localhost and 0.0.0.0

"""

from impacket import ImpactPacket, ImpactDecoder
import optparse
import re
import socket
import string


def PrintManual():
    manual = '''
    Manual:

    This tool is a basic port scanner implemented using the Impacket library.
    '''
    print(manual)

def send_UDP_packets():
    print("\n[+] Preparing to create UDP packets.")
    print("[!] Not yet implemented.\n")

def send_ping(source_ip, dest_ip):
    print(f"\n[+] Preparing to send a ping from {source_ip} to {dest_ip}.\n")
    

def main():
    # Set up basic flags as per Didier's template, though likely not using many of them.
    oParserFlag = optparse.OptionParser(usage="\nFlag arguments start with #f#:")
    oParserFlag.add_option("-l", "--length", action="store_true", default=False, help="Print length of files")

    # Create the main argument parser
    oParser = optparse.OptionParser(usage="usage: %prog [options]")
    oParser.add_option("-m", "--man", action="store_true", default=False, help="Print Manual")
    oParser.add_option("-u", "--UDP", action="store_true", default=False, help="Send UDP packets")
    oParser.add_option("-p", "--ping", action="store_true", default=False, help="Send an ICMP ping")

    (options, args) = oParser.parse_args()
    print((options, args))
#    print(len(args))
#    print(args[1])

    if options.man:
        PrintManual()
        return
    if options.UDP:
        send_UDP_packets()
        return
    if options.ping:
        # If there aren't 2 arguments, then they didn't include the src and dest ip addresses
        if len(args) < 2:
            print(f"Use: scanner.py -p <src ip> <dest ip>")
        else:
            send_ping(args[0], args[1])
        return

if __name__ == "__main__":
    main()