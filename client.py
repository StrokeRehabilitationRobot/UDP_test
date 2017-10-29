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
#print message
data = pack('<f',5)


#buf = struct.pack('%sf' % len(floatlist), *floatlist)

floatlist = [2 for _ in range(15)]
cmd = 37

while 1:
    buf = struct.pack('%sf' % len(floatlist), *floatlist)
    print buf
    buf2 = struct.pack('i' , cmd) 
    print buf2 + buf
    sent = sock.sendto(buf2 + buf, server_address)
    data, server = sock.recvfrom(4096)
    #print data
    print array.array('d',data )




