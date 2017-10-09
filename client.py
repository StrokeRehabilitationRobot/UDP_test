import socket
import sys
import base64
import struct
import array

from struct import *


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9876)
message = array.array('d', [6,5])
message = pack('ffff', 0, 2, 3,4)

while 1:


    # Send data

    print >>sys.stderr, 'sending "%d"' % 37
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print array.array('d',data )


    # finally:
    #     print >>sys.stderr, 'closing socket'
    #     sock.close()
