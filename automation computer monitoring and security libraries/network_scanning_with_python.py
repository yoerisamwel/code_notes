from scapy.all import IP, ICMP, sr1

# Function to perform a simple ping to check if a host is online
def ping(host):
    # Creating an ICMP packet to the target host
    packet = IP(dst=host)/ICMP()
    # Sending the packet and waiting for a reply
    response = sr1(packet, timeout=2, verbose=0)
    # If a response is received, the host is online
    if response:
        return f"{host} is online"
    # If no response is received, the host is considered offline
    else:
        return f"{host} is offline"

# Example usage
host_to_scan = "example.com"
result = ping(host_to_scan)
print(result)

# Explanation with use cases:
'''
# Network Scanning with Scapy:

Scapy is a powerful Python-based interactive packet manipulation program and library. It is used to handle tasks like network scanning, packet sniffing, and network discovery.

Use cases:

1. Network Discovery: System administrators can use it to scan their networks, identifying active devices and their configurations.
   Example: A script that runs through an IP range to identify which hosts are online.

2. Security Testing: Security professionals can use Scapy to test network defenses and detect vulnerabilities by crafting malicious packets.
   Example: Penetration testers mimic network attacks to evaluate the effectiveness of security measures.

3. Traffic Analysis: It can be used to analyze network traffic to understand the types of traffic on a network and identify any anomalies.
   Example: A network analyst monitors traffic for unusual patterns that could indicate a security breach.

4. Educational Purposes: Due to its versatility and depth, Scapy is also often used as a teaching tool for network protocols and concepts.
   Example: Students practice building custom packets to understand the underlying protocol structures.

The provided code implements a simple network scanning function using Scapy that sends an ICMP echo request (ping) to a specified host and checks for a response to determine if the host is online or offline.
'''