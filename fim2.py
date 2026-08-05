import os
import time
import hashlib

def calcular_sha256(caminho_arquivo):
    """Gera uma impressão digital (hash) SHA-256 única para um arquivo."""
    sha256_hash = hashlib.sha256()
    try:
        with open(caminho_arquivo, "rb") as f:
            for bloco_bytes in iter(lambda: f.read(4096), b""):
                sha256_hash.update(bloco_bytes)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

# Arquivo que será monitorado
arquivo_alvo = "arquivo_importante_do_sistema.txt"

# Monitorar um arquivo local para detectar modificações não autorizadas
diretorio_script = os.path.dirname(os.path.abspath(__file__))
diretorio_monitoramento = os.path.join(diretorio_script, "fim")
arquivo_alvo = os.path.join(
    diretorio_monitoramento,
    "arquivo_importante_do_sistema.txt"
)

print(f"Iniciando linha de base do FIM para {arquivo_alvo}...")

# Criar o arquivo caso ele não exista (apenas para testes)
os.makedirs(diretorio_monitoramento, exist_ok=True)

if not os.path.exists(arquivo_alvo):
    with open(arquivo_alvo, "w") as f:
        f.write("Estado inicial seguro da configuração.")

hash_base = calcular_sha256(arquivo_alvo)

try:
    while True:
        time.sleep(5)  # Verifica o arquivo a cada 5 segundos
        hash_atual = calcular_sha256(arquivo_alvo)

        if hash_atual is None:
            print("🚨 ALERTA: O arquivo monitorado foi excluído!")
            break

        elif hash_atual != hash_base:
            print("🚨 ALERTA: Modificação detectada no arquivo! Integridade comprometida.")

            # Atualiza a linha de base para registrar o novo estado conhecido
            # ou evitar alertas contínuos
            hash_base = hash_atual

        else:
            print("Arquivo seguro. Nenhuma alteração detectada.")

except KeyboardInterrupt:
    print("Monitoramento encerrado.")
