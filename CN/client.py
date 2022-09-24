""" import socket
s=socket.socket()
s.connect((socket.gethostname(), 12345))
num=input("Enter number: ")
s.send(num.encode())
msg=s.recv(20)
print(msg.decode())
s.close()
 """
# ///////////// Tcp client for seaser cipher ////////////	
import socket
s=socket.socket()
s.connect((socket.gethostname(), 12345))
num=input("Enter String: ")
key=input("Enter Key: ")
option=input("Enter 1 for Encryption and 2 for Decreption : ")
s.send(num.encode())
s.send(key.encode())
s.send(option.encode())
msg=s.recv(20)
print(msg.decode())
s.close() 



""" 
import socket
s=socket.socket()
s.connect((socket.gethostname(), 12345))
num=input("Enter String: ")
key=input("Key String: ")
option=input("Enter 1 for Encryption and 2 for Decreption : ")
s.send(num.encode())
s.send(key.encode())
s.send(option.encode())
msg=s.recv(1024)
print(msg.decode())
s.close()
 """