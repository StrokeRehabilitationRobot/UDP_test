import socket
import sys
import base64
import struct
import array
import  pickle
from struct import *
import random


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9876)
message = pickle.dumps(['5','5','5','5','5'])
#print message
data = pack('<f',5)


#buf = struct.pack('%sf' % len(floatlist), *floatlist)

while 1:
    floatlist = [random.random() for _ in range(15)]
    buf = struct.pack('%sf' % len(floatlist), *floatlist)
    sent = sock.sendto(buf, server_address)
    data, server = sock.recvfrom(4096)
    #print data
    print array.array('d',data )
