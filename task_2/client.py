"""
Authors:
    Rodrigo Martin Sziller
    Lior Mahfoda
"""

import socket
import time
from random import randint
import math


def sxor(s1, s2):
    if (s1 == 0):
        return s2
    if (s2 == 0):
        return s1
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


udpIp = "127.0.0.1"
udpPort = 12321
packetSize = 100
sequenceLen = 4
msg = "Make it totally clear that this gun has a right end and a wrong end.\n" \
      "Make it totally clear to anyone standing at the wrong end that things are going badly for them.\n" \
      "If that means sticking all sort of spikes and prongs and blackened bits all over it then so be it.\n" \
      "This is not a gun for hanging over the fireplace or sticking in the umbrella stand,\n" \
      "it is a gun for going out and making people miserable with."

print ("UDP target IP:", udpIp)
print ("UDP target port:", udpPort)

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
data_size = (packetSize - sequenceLen - 1)
packets_len = int(math.ceil(len(msg) / float(data_size)))
while True:
    d = randint(2, packets_len)
    sock.sendto(str(d), (udpIp, udpPort))
    print ("\nclient sent random number d to server")
    print ("d = ", d)
    e_count = int(math.ceil(packets_len / float(d)))
    e = 0
    len1 = packets_len + e_count
    e_i = 1
    msg_i = 0
    print ("The client begins to send the message to the server")
    for i in reversed(range(len1)):
        if (i == 0 or e_i == d + 1):
            sock.sendto(("{0:0" + str(sequenceLen) + "d}").format(i) + "#" + e, (udpIp, udpPort))
            e = 0
            e_i = 1
        else:
            _msg = msg[msg_i:msg_i + (data_size)]
            if (e_i != d and i != 1):
                sock.sendto(("{0:0" + str(sequenceLen) + "d}").format(i) + "#" + msg, (udpIp, udpPort))
            msg_i += data_size
            e = sxor(e, msg)
            e_i += 1

        print ("\nThe client sent packet #", i)
        time.sleep(1)
    print ("\nThe client has finished to send the message to the server.")
    print ("\nThe client waits for the server to send back the message lines.")
    for i in range(len(msg.split('\n'))):
        data, addr = sock.recvfrom(10000)
        print ("\nThe client received line:", data)
    print ("\nThe client received all the data lines from the server")
    print ("\nThe client waits 3 seconds...")
    time.sleep(3)
