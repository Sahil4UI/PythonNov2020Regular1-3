import socket

s= socket.socket()

port =9999
s.bind(('localhost',port))
print("Socket binding to port")


s.listen(5)
print("socket is listening")


msg="Thanx for connecting.."


while True:
    conn,address  = s.accept()
    print("Got connection from ",address)
    conn.send(msg.encode())
    conn.close

