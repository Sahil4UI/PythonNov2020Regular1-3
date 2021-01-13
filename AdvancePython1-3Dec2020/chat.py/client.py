import socket

s= socket.socket()
port=9999

s.connect(('localhost',port))
chat=True
while chat==True:
    msg=input("Enter Message : ")
    if msg=="quit":
        chat=False
        
    s.send(msg.encode())
    data = s.recv(1024).decode()
    print("Server : ",data)
        
s.close()
