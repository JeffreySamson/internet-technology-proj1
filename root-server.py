import threading
import time
import random

import socket

try:
    rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[RS]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', 50001)
rs.bind(server_binding)
rs.listen(1)
host = socket.gethostname()
print("[RS]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[RS]: Server IP address is {}".format(localhost_ip))
csockid, addr = rs.accept()
print ("[RS]: Got a connection request from a client at {}".format(addr))

DNS = {
    'hostNane': ['qtsdatacenter.aws.com', 'mx.rutgers.edu', 'kill.cs.rutgers.edu', 
                    'www.ibm.com', 'www.google.com', 'localhost'],
    'ipAddress': ['128.64.3.2', '192.64.4.2', '182.48.3.2', '64.42.3.4', '8.6.4.2', '-'],
    'flag': ['A', 'A', 'A', 'A', 'A', 'NS']
}

msg = rs.recv(100)
print(msg.decode('utf-8'))