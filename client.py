import socket
import sys

HOST = "127.0.0.1"
PORT = None

try:
    PORT = 40404
except IndexError:
    print("Pass a port for connection")
    exit(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    print(f"Connecting to {HOST}:{PORT}")
    server.connect((HOST, PORT))
    data = server.recv(1024)
    print(repr(data))
    server.close()