# Equipe B - Descriptografar mensagem e verificar assinatura
import rsa
import os

# --- Configurações ---
ARQ_CHAVE_PUBLICA_A = "chaves/chave_publica_a.pem"
ARQ_CHAVE_PRIVADA_B = "chaves/chave_privada_b.pem"
ARQ_MENSAGEM_CRIPTO = "mensagens/mensagem_cripto.txt"
ARQ_ASSINATURA = "mensagens/assinatura.bin"
ARQ_MENSAGEM_RECEBIDA = "mensagens/mensagem_recebida.txt"
ARQ_VERIFICACAO = "mensagens/assinatura_verificada.txt"

# Carrega chaves
with open(ARQ_CHAVE_PUBLICA_A, "rb") as f:
    chave_publica_a = rsa.PublicKey.load_pkcs1(f.read())

with open(ARQ_CHAVE_PRIVADA_B, "rb") as f:
    chave_privada_b = rsa.PrivateKey.load_pkcs1(f.read())

# Lê mensagem criptografada
with open(ARQ_MENSAGEM_CRIPTO, "rb") as f:
    mensagem_cripto = f.read()

# Descriptografa
try:
    mensagem = rsa.decrypt(mensagem_cripto, chave_privada_b)
    with open(ARQ_MENSAGEM_RECEBIDA, "wb") as f:
        f.write(mensagem)
    print("✅ Mensagem descriptografada com sucesso.")
except Exception as e:
    print(f"❌ Erro na descriptografia: {e}")
    exit()

# Lê assinatura
with open(ARQ_ASSINATURA, "rb") as f:
    assinatura = f.read()

# Verifica assinatura
try:
    rsa.verify(mensagem, assinatura, chave_publica_a)
    resultado = "SUCESSO: Assinatura VÁLIDA."
    print("✅ Assinatura verificada com sucesso.")
except rsa.VerificationError:
    resultado = "FALHA: Assinatura INVÁLIDA."
    print("❌ Assinatura inválida.")

# Salva resultado
with open(ARQ_VERIFICACAO, "w") as f:
    f.write(resultado)
    f.write("\n\nMensagem:\n" + mensagem.decode("utf-8"))
