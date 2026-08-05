import socket
import sys

alvo = "127.0.0.1"  # Verifica com segurança o endereço de loopback local
portas_para_verificar = [21, 22, 80, 443, 8080]

print(f"Verificando alvo: {alvo}")

for porta in portas_para_verificar:
    # AF_INET especifica IPv4 e SOCK_STREAM especifica o protocolo TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)  # Evita travar em endereços que não respondem

    resultado = sock.connect_ex((alvo, porta))
    if resultado == 0:
        print(f"🔓 Porta {porta}: ABERTA")
    else:
        print(f"🔒 Porta {porta}: Fechada/Filtrada")

    sock.close()
