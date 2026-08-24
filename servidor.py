import socket

HOST = 'localhost'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Conectado a {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Mensagem do Cliente: {message}")
    communication_socket.send("Mensagem recebida com Sucesso!".encode('utf-8'))
    communication_socket.close()
    print(f"Conexão com {address} encerrada!")