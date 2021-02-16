import threading
import time
import random
import sys

import socket

# client for root server
try:
    crs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[CRS]: Client socket for RS created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# port and hostname from cmd line argument
rs_port = int(sys.argv[2])
rshost_addr = socket.gethostbyname(sys.argv[1])

# connect to rs
rs_binding = (rshost_addr, rs_port)
crs.connect(rs_binding)

#JEFF's CODE
#target = input("Enter the dns name you want to find: ")
#with open('PROJI-HNS.txt', 'r') as f:
#    read_file = f.readlines()

#msg = ""
#for line in read_file:
    #print(line.strip('\n'))
#    if line.strip('\n') == target:
#        msg = line.rstrip("\r\n")
#        break
#    else:
#        msg = 'Hostname - Error:HOST NOT FOUND'
#crs.send(msg.encode('utf-8'))

# read input file
with open('PROJI-HNS.txt', 'r') as f:
    read_file = f.readlines()

# send a intro message to the client.
n = random.randint(0,len(read_file)-1)
msg = read_file[n].rstrip("\r\n")
crs.send(msg.encode('utf-8'))

# Receive data from the server
data_from_rs = crs.recv(100)
decoded_msg = data_from_rs.decode('utf-8')
print("[C]: Data received from root-server: " + str(decoded_msg))

# write received data to outupt file if DNS is resolved
if "A" in decoded_msg:
    with open('resolve.txt', 'a') as text_file:
        text_file.write(decoded_msg + "\n")

name = "localhost - NS".split(" ")

# client for top-level server
# time.sleep(5)
try:
    cts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[CTS]: Client socket for TS created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

ts_port = int(sys.argv[3])

if "NS" in decoded_msg:
    host = name[0]
else:
    host = socket.gethostname()

#print(host)

localhost_addr = socket.gethostbyname(host)
server_binding = (localhost_addr, ts_port)
cts.connect(server_binding)

cts.send(msg.encode('utf-8'))

# Receive data from the server
data_from_ts = cts.recv(100)
decoded = data_from_ts.decode('utf-8')
print("[C]: Data received from top-level-server: " + str(decoded))

# write received data to outupt file
with open('resolve.txt', 'a') as text_file:
    text_file.write(decoded + "\n")
