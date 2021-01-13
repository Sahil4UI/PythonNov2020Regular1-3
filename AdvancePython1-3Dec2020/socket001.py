import socket
import sys

#stream-> flow of bytes
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Created Successfully")

port =80
try:
    host_ip = socket.gethostbyname("www.google.com")
    s.connect((host_ip,80))
    print("Successfully Connected : ")
except socket.gaierror:
    print("Error")
    sys.exit()