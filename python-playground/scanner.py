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
import select
import socket
import time

def PrintManual():
    manual = '''
    Manual:

    This tool is a basic port scanner implemented using the Impacket library.

    Flags:
     -l, --length: Print length of a file. Not used.
     -u, --UDP: Send a UDP packet. Not yet implemented (NYI).
     -p, --ping: Send a ping. Requires a soure and destination address.
     -m, --man: This manual.
    '''
    print(manual)

def send_UDP_packets():
    print("\n[+] Preparing to create UDP packets.")
    print("[!] Not yet implemented.\n")

def send_ping(source_ip, dest_ip):
    print(f"\n[+] Preparing to send a ping from {source_ip} to {dest_ip}.\n")
    
    # Create a new packet, based on example code from the Impacket repo
    try:
        ip_packet = ImpactPacket.IP()
    except:
        print("[!] Couldn't create IP packet with Impacket.")
        exit(-1)
    finally:
        ip_packet.set_ip_src(source_ip)
        ip_packet.set_ip_dst(dest_ip)

    # Create an ICMP packet of type ECHO
    icmp_packet = ImpactPacket.ICMP()
    icmp_packet.set_icmp_type(icmp_packet.ICMP_ECHO)

    # Add a 156-character payload (not sure why 156?)
    icmp_packet.contains(ImpactPacket.Data(b"A"*156))

    # Put the ICMP packet inside the IP packet.
    ip_packet.contains(icmp_packet)

    # Open a raw socket, which might need admin priv on Windows.
    # Requires raw (BSD) socket coding: https://docs.python.org/3/library/socket.html
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    packet_id = 1
    for packet_id in range(1, 5):
        # Give the ICMP packet the next (sequential) ID in the sequence
        icmp_packet.set_icmp_id(packet_id)

        # Calculate the checksum
        # C implementation: https://www.cs.dartmouth.edu/~sergey/cs60/lab3/icmp4-rawsend.c
        icmp_packet.set_icmp_cksum(0)
        icmp_packet.auto_checksum = 1

        # Send it to the destination
        s.sendto(ip_packet.get_packet(), (dest_ip, 0))

        # Wait for replies
        if s in select.select([s], [], [],)[0]:
            reply = s.recvfrom(2000)[0]

            # Use ImpacketDecoder to reconstruct the packet
            response_ip_packet = ImpactDecoder.IPDecoder().decode(reply)
            response_icmp_packet = response_ip_packet.child()

            # If it matches, report it to the user
            if response_ip_packet.get_ip_dst() == source_ip and response_ip_packet.get_ip_src() == dest_ip and icmp_packet.ICMP_ECHOREPLY == response_icmp_packet.get_icmp_type():
                print(f"Ping reply for sequence {response_icmp_packet.get_icmp_id()}")

            # Add a delay before sending the next packet. Maybe this should be customizable.
            time.sleep(1)


def main():
    print("[#] You can use python scanner.py -p 192.168.2.21 172.217.1.14 as a test")
    # Set up basic flags as per Didier's template, though likely not using many of them.
    oParserFlag = optparse.OptionParser(usage="\nFlag arguments start with #f#:")
    oParserFlag.add_option("-l", "--length", action="store_true", default=False, help="Print length of files")

    # Create the main argument parser
    oParser = optparse.OptionParser(usage="usage: %prog [options]")
    oParser.add_option("-m", "--man", action="store_true", default=False, help="Print Manual")
    oParser.add_option("-u", "--UDP", action="store_true", default=False, help="Send UDP packets")
    oParser.add_option("-p", "--ping", action="store_true", default=False, help="Send an ICMP ping")

    (options, args) = oParser.parse_args()
#    print((options, args))
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