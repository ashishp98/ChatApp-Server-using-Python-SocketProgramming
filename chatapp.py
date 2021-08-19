import socket
import threading
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 4321
ip = ""
s.bind((ip, port))

s.listen()

def chatapp(session_data, client_data):
    # print(session_data)
    # print(client_data)
    print()
    print(f"client {client_data[0]} has connected")
    # session_data.send(b"Hello Client, I am Server ")
    msg = ""
    while True:
        client_msg = session_data.recv(1024)
        client_msg_decoded = client_msg.decode()
        print(client_data[0], end=" : ")
        print(client_msg_decoded)
        if ("exit" in client_msg_decoded):
            print("Client exited")
            sys.exit()
            #return None
        else:
            pass
        session_data.send(input(f"Enter the message to {client_data[0]}: ").encode())
       

"""       
        if ("exit" in client_msg_decoded):
            print("Client exited")
            sys.exit() 
            #return None
        else:
            pass
"""


while True:
    session_data, client_data = s.accept()
    t1 = threading.Thread(target = chatapp, args = (session_data, client_data))
    t1.start()
