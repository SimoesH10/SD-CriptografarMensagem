# Equipe A - Criptografar mensagem e assinar digitalmente
import rsa
import os

# --- Configurações ---
ARQ_CHAVE_PUBLICA_B = "chaves/chave_publica_b.pem"
ARQ_CHAVE_PRIVADA_A = "chaves/chave_privada_a.pem"
ARQ_MENSAGEM = "mensagens/mensagem.txt"
ARQ_MENSAGEM_CRIPTO = "mensagens/mensagem_cripto.txt"
ARQ_ASSINATURA = "mensagens/assinatura.bin"

os.makedirs("mensagens", exist_ok=True)

# Carrega a chave pública da Equipe B
with open(ARQ_CHAVE_PUBLICA_B, "rb") as f:
    chave_publica_b = rsa.PublicKey.load_pkcs1(f.read())

# Carrega a chave privada da Equipe A
with open(ARQ_CHAVE_PRIVADA_A, "rb") as f:
    chave_privada_a = rsa.PrivateKey.load_pkcs1(f.read())

# Lê a mensagem original
with open(ARQ_MENSAGEM, "rb") as f:
    mensagem = f.read()

# Criptografa a mensagem com a chave pública da Equipe B
mensagem_cripto = rsa.encrypt(mensagem, chave_publica_b)
with open(ARQ_MENSAGEM_CRIPTO, "wb") as f:
    f.write(mensagem_cripto)

# Assina a mensagem original
assinatura = rsa.sign(mensagem, chave_privada_a, 'SHA-256')
with open(ARQ_ASSINATURA, "wb") as f:
    f.write(assinatura)

print("✅ Mensagem criptografada e assinada com sucesso.")
