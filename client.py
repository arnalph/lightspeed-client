import socket
import logging as log
import sys
import os
import psutil
import time

class Client(object):
    def __init__(self, sock, host, gac, port):
        self.sock = sock
        self.host = host
        self.gac = gac
        self.port = port
        self.pid = os.getpid()
        self.url = ''

    def connect(self):
        self.sock.connect((self.host,self.port))
        self.sock.sendall(bytes(self.gac,'utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        print(data)
        self.url=data
        d = self.sock.recv(1024).decode('utf-8')
        rungame("rtsp://127.0.0.1:8554/man")
        
def rungame(url):
        time.sleep(20)
        os.chdir("D:/g7/bin/")
        os.system('start ga-client config/client.abs.conf '+url)
        
