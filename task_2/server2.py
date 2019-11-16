"""
Authors:
    Rodrigo Martin Sziller
    Lior Mahfoda
"""

import socket
import time


def sxor(s1, s2):
    if (s1 == 0):
        return s2
    if (s2 == 0):
        return s1
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def lxor(l):
    ret = l[0]
    for i in range(1, len(l)):
        ret = sxor(ret, l[i])
    return ret


udpIp = "127.0.0.1"
udpPort = 12321
sequenceLen = 4
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((udpIp, udpPort))

print ("The server is listening to port ", udpPort)
while True:
    msg = ""
    data, addr = sock.recvfrom(100)
    d = int(data)
    print ("\nserver received random number d from client")
    print ("\nd =", d)
    data, addr = sock.recvfrom(100)
    print ("The server begins to receive data from ", addr[0], ":", addr[1])
    m = [0] * (d + 1)
    next_e = int(data[:sequenceLen]) - d
    e_i = 0
    m[e_i] = data
    while int(data[:sequenceLen]):
        print ("\nThe server has received packet #", int(data[:sequenceLen]))
        if (int(data[:sequenceLen]) == next_e):
            next_e = int(data[:sequenceLen]) - d - 1
            m[e_i] = lxor(m)
            for x in m:
                if (x == 0):
                    break
                msg += x[sequenceLen + 1:]
            e_i = -1
            m = [0] * (d + 1)
        data, addr = sock.recvfrom(100)
        e_i += 1
        m[e_i] = data
    m[e_i] = lxor(m)
    for x in m:
        if (x == 0):
            break
        msg += x[sequenceLen + 1:]

    print ("\nThe server has received packet #", int(data[:sequenceLen]))
    print ("\nThe server starts to echo the data lines.")
    for m in msg.split('\n'):
        sock.sendto(m, addr)
        print ("\nThe server has echoed", m)
        time.sleep(1)
