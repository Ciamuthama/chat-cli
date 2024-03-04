import socket
import sys

HOST,PORT ="localhost", 8092

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))
        data = input("type...")
        sock.sendall(bytes(data + '\n', "utf-8"))
        
        received = str(sock.recv(1024), "utf-8")
        print("You: {}".format(data))
        print("other you: {}".format(received))