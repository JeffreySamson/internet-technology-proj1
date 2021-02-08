import threading
import time
import random

import socket

# client for root server
try:
    crs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[CRS]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

port = 50001
localhost_addr = socket.gethostbyname(socket.gethostname())
server_binding = (localhost_addr, port)
crs.connect(server_binding)
csockid, addr = crs.accept()

msg = "qtsdatacenter.aws.com"
print(msg)
csockid.send(msg.encode('utf-8'))


# client for top-level server
time.sleep(5)
try:
    cts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[CTS]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

port = 50007
localhost_addr = socket.gethostbyname(socket.gethostname())
server_binding = (localhost_addr, port)
cts.connect(server_binding)

# "main method"

#if __name__ == "__main__":
#    t1 = threading.Thread(name='root-server', target=server)
#    t1.start()

#    time.sleep(random.random() * 5)
#    t2 = threading.Thread(name='top-level-server', target=server)
#    t2.start()

#    t3 = threading.Thread(name='client', target=client)
#    t3.start()

#    time.sleep(5)
#    print('done')