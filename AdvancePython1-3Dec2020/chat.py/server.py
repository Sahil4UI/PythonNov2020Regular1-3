import socket

s=socket.socket()
port=9999
s.bind(('localhost',port))
s.listen(3)
print("Socket is listening")
conn,address=s.accept()
print("Got connection from ",address)
while True:
    data=conn.recv(1024).decode()
    if not data:
        print("No data")
        break
    print("Client : ",data)

    msg=input("Enter you msg : ")
    conn.send(msg.encode())
conn.close()