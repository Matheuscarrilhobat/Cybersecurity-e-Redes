import random
import string

Alfabeto = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits + " ")

def gerar_chave(alfabeto):
    alfabeto_embaralhado = alfabeto.copy()
    random.shuffle(alfabeto_embaralhado)
    return alfabeto_embaralhado

def encriptar(texto, chave, alfabeto):
    texto_encriptado = [chave[alfabeto.index(c)] for c in texto]
    return ''.join(texto_encriptado)

def desencriptar(texto, chave, alfabeto):
    texto_desencriptado = [alfabeto[chave.index(c)] for c in texto]
    return ''.join(texto_desencriptado)

chave_gerada = gerar_chave(Alfabeto)
print(chave_gerada)

texto_original = str(input("Digite a mensagem que deseja encriptar: "))

mensagem_encriptada = encriptar(texto_original, chave_gerada, Alfabeto)

print("Mensagem encriptada:", mensagem_encriptada)

mensagem_desencriptada = desencriptar(mensagem_encriptada, chave_gerada, Alfabeto)
print("Mensagem desencriptada:", mensagem_desencriptada)