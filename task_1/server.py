"""
Authors:
    Rodrigo Martin Sziller
    Lior Mahfoda
"""

import socket
import time

udpIp = "127.0.0.1"
udpPort = 12321
sequenceLen = 4
msg = ""
_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
_socket.bind((udpIp, udpPort))

print ("The server is listening to port ", udpPort)
while True:
    msg = ""
    data, addressess = _socket.recvfrom(100)
    print ("The server begins to receive data from ", address[0], ":", address[1], ".")
    print ("\nThe server has received packet #", int(data[:sequenceLen]), ".")
    msg += data[sequenceLen + 1:]
    while int(data[:sequenceLen]):
        data, address = _socket.recvfrom(100)
        msg += data[sequenceLen + 1:]
        print ("\nThe server has received packet #", int(data[:sequenceLen]), ".")
    print ("\nThe server starts to echo the data lines.")
    for m in msg.split('\n'):
        _socket.sendto(m, address)
        print ("\nThe server has echoed", m)
        time.sleep(1)
