import socket
import sys

alvo = "127.0.0.1" 
portas_para_verificar = [21, 22, 80, 443, 8080]

print(f"Verificando alvo: {alvo}")

for porta in portas_para_verificar:
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)  # Evita travar em endereços que não respondem

    resultado = sock.connect_ex((alvo, porta))
    if resultado == 0:
        print(f"Porta {porta}: ABERTA")
    else:
        print(f"Porta {porta}: Fechada/Filtrada")

    sock.close()
