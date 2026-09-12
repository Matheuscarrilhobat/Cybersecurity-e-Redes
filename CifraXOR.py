def xor_cipher(text, key):
    if isinstance(text, str):
        text = text.encode()

    if len(key) < len(text):
        key = key * (len(text) // len(key) + 1)
        key = key[:len(text)]

    return bytes([x ^ y for x, y in zip(text, key)])

original_text = input("Digite o texto para cifrar: ")

key = b'chavesegura'

encrypted = xor_cipher(original_text, key)

print("Texto cifrado:", encrypted)

decrypted = xor_cipher(encrypted, key)

print("Texto decifrado:", decrypted.decode())