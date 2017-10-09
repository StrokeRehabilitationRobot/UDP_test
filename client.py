import socket
import sys
import base64
import struct
import array




# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9876)
message = 37

while 1:


    # Send data
    if message is '37':
        message = '38'
    elif message is '38':
        message = '37'
    print "hello"
    print >>sys.stderr, 'sending "%i"' % 37
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print array.array('d',data )

    # finally:
    #     print >>sys.stderr, 'closing socket'
    #     sock.close()
