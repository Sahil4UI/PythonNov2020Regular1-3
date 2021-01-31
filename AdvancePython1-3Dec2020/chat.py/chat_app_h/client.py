import socket
import sys

def main():
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host="localhost"
    port=9999
    
    try:
        soc.connect((host,port))
    except:
        print("connection Error")
        sys.exit()
    
    print("#you can Enter 'quit' to exit")
    username = input("Enter UserName : ")
    soc.sendall(username.encode("utf8"))
    message = input("-->")
    
    while message != 'quit':
        soc.sendall(message.encode("utf8"))
        data = soc.recv(1024)
        print(data.decode())
        message = input("->")
    soc.send(b'--quit--')
    
main()