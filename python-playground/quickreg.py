"""Quick and Dirty Regex Testing"""

import re

message = "The quick brown fox fox jumped over the lazy dog."

pattern = ".*fox.*"
#pattern = "fox" # Not found

p = re.compile(pattern)
print(f"Compiled pattern: {p}")

if (p.match(message)):
    print(f"Pattern '{pattern}' was found.")
else:
    print("Not found.")

fox = "fox"
result = re.findall(fox, message)
print(result)
if result:
    print(f"The pattern '{fox}' was found in the message.")


def find_ip_addresses(string): #usually could take bytes
    # IP address pattern from Claude.ai
    strict_ipv4 = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    
    results = re.findall(strict_ipv4, str(string))
    print(f"IP Addresses: {results}")


bad_script = """
somethiong = blah bala 192.168.3.10 10.2.4.5
IEX (New-Object IO.StreamReader(New-Object IO.Compression.GzipStream($s,[IO.Compression.CompressionMode]::Decompress))).ReadToEnd();
"""
find_ip_addresses(bad_script)