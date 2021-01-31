import socket
import sys
import traceback
from threading import Thread

def main():
    start_server()
    
def start_server():
    host = "localhost"
    port = 9999
    
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # SO_REUSEADDR flag tells kernelto resue a local socket in time_wait state,
    # without waiting for its timout to expire
    print("socket create")
    
    
    try:
        soc.bind((host,port))
    except:
        print("Binding Failed Error : "+str(sys.exc_info()))
        sys.exit()
    
    soc.listen(5)
    print("Socket is now Listening...")
    
    while True:
        connection,address = soc.accept()
        ip,port =str(address[0]),str(address[1])
        print("Connected with "+ip+" : "+port)
        
        try:
            Thread(target=client_thread , args=(connection,ip,port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()
    soc.close()
    
def client_thread(connection,ip,port,max_buffer_size=5120):
    is_active = True
    
    while is_active:
        client_input = receive_input(connection,max_buffer_size)
        
        if "--QUIT--" in client_input:
            print("client is requesting to quit")
            connection.close()
            print("Connected with "+ip+" : "+port+"is closed")
            is_active = False
        else:
            print("Processed Result : {} ".format(client_input))
            msg = input("->")
            connection.sendall(msg.encode("utf-8"))
            
def receive_input(connection,max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    
    if client_input_size > max_buffer_size:
        print("the input size is greater than Buffer Size")
    
    decoded_input = client_input.decode("utf-8").rstrip()
    result = process_input(decoded_input)
    return result
    

def process_input(input_str):
    print("Processing the input recieved from Client")
    return "Hello"+str(input_str).upper()



main()