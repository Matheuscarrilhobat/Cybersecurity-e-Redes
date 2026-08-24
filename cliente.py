import socket

HOST = 'localhost'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Olá, Servidor!".encode('utf-8'))
print("Mensagem enviada ao Servidor!")
print(socket.recv(1024).decode('utf-8'))