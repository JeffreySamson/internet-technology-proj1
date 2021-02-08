import threading
import time
import random

import socket

try:
    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[TS]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', 50007)
ts.bind(server_binding)
ts.listen(1)
host = socket.gethostname()
print("[TS]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[TS]: Server IP address is {}".format(localhost_ip))
csockid, addr = ts.accept()
print ("[TS]: Got a connection request from a client at {}".format(addr))
