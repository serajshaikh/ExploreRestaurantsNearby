import socket
import socket
from threading import Thread


def send():
    while True:
        msg=input("Enter message: ")
        s.send(msg.encode())
        if msg=="{quit}":
            break

def receive():
    while True:
        msg=s.recv(1024).decode()
        if msg=="{quit}":
            s.close()
            break
        if not msg:
            break
        else:
            print(msg)



s=socket.socket()
s.connect((socket.gethostname(),12345))
recv_thread=Thread(target=receive)
send_thread=Thread(target=send)
recv_thread.start()
recv_thread.join()

