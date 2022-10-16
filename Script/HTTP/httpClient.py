from random import randint
import socket
import sys

socket.setdefaulttimeout(3)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((sys.argv[1], int(sys.argv[2])))
    website = randint(0, 499)
    msg = 'GET ' + str(website) + ' HTTP/1.1'
    s.sendall(msg.encode('utf-8'))

    try:
        print(s.recv(4096).decode('utf-8'))
    except:
        s.close()
        sys.exit()