"""
Authors:
    Rodrigo Martin Sziller
    Lior Mahfoda
"""

from scapy.all import *
import sys

sequenceLen = 5


def print_packet(p):
    pl = str(p[UDP].payload)
    print p.sprintf("\n%IP.src%:%UDP.sport% -> %IP.dst%:%UDP.dport%")
    print "data:", pl


sniff(filter="udp and host 127.0.0.1", prn=print_packet)
