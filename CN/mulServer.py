from os import name
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
def accept_incomming_connection():
    k,a=s.accept()
    print(f"connected to {a}")
    k.send('Welcome to the server please type your Name: '.encode())
    address[k]=a
    Thread(target=handle_client, args=(k,)).start()


def handle_client(k):
    name=k.recv(1024).decode()
    welcome=f"Welcome to {name}, type '{quit}' if u want to exit: "
    k.send(welcome.encode())
    broadcost(msg.encode())
    clients[k]=name
    while True:
        msg=k.recv(1024).decode()
        if msg!="{quit}":
            broadcost(msg, name+":")
        else:
            k.send("\"{quit}\"")
            k.close()
            del clients[k]
            broadcost(f"{name} has left the chat".encode())
            break
def broadcost(msg,prefix=""):
    for i in clients:
        i.send((prefix+msg).encode())








s=socket(AF_INET,SOCK_STREAM)
host=12345
hostname=''
s.bind((hostname, host))
address={}
clients={}

if __name__ == "__main__":
    s.listen(1024)
    print("waiting for incomming connections ")
    Accept_Thread=Thread(target=accept_incomming_connection)
    Accept_Thread.start()
    Accept_Thread.join()
    s.close()
