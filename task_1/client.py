"""
Authors:
    Rodrigo Martin Sziller
    Lior Mahfoda
"""

import socket
import math
import time

udpIp = "127.0.0.1"
udpPort = 12321
packetSize = 100
sequenceLen = 4
msg = "It is known that there are an infinite number of worlds,\n" \
      "simply because there is an infinite amount of space for them to be in.\n" \
      "However, not every one of them is inhabited.\n" \
      "Therefore, there must be a finite number of inhabited worlds.\n" \
      "Any finite number divided by infinity is as near to nothing as makes no odds,\n" \
      "so the average population of all the planets in the Universe can be said to be zero.\n" \
      "From this it follows that the population of the whole Universe is also zero,\n" \
      "and that any people you may meet from time to time are merely the products of a deranged imagination."

print "UDP target IP:", udpIp
print "UDP target port:", udpPort

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data_size = (packetSize - sequenceLen - 1)
packets_len = int(math.ceil(len(msg) / float(data_size)))
packets = [("{0:0" + str(sequenceLen) + "d}").format(packets_len - (i // data_size) - 1) + "#" + msg[i:i + data_size]
           for i in range(0, len(msg), data_size)]

while True:
    print "The client begins to send the message to the server"
    for packet in packets:
        sock.sendto(packet, (udpIp, udpPort))
        print "\nThe client sent packet #", int(packet[:sequenceLen])
        time.sleep(1)
    print "\nThe client has finished to send the message to the server."
    print "\nThe client waits for the server to send back the message lines."
    for i in range(len(msg.split('\n'))):
        data, addr = sock.recvfrom(10000)
        print "\nThe client received line:", data
    print "\nThe client received all the data lines from the server"
    print "\nThe client waits 3 seconds..."
    time.sleep(3)
