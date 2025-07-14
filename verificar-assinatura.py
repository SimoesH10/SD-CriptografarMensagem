import rsa
import base64

# === Carregar a chave privada da Equipe B ===
with open("chaves/chave_privada_a.pem", "rb") as priv_file:
    chave_privada_b = rsa.PrivateKey.load_pkcs1(priv_file.read())

# === Carregar a chave pública da Equipe A ===
chave_publica_a_pem = """
-----BEGIN RSA PUBLIC KEY-----
MEgCQQCur00bYIZEKas+lyDeraMDbxDjRLqDED5bK7e5WB3toLsSP8H1FwhVfhrL
vIaeqE7wk/+8lol/NMxQHWKTlXatAgMBAAE=
-----END RSA PUBLIC KEY-----
"""
chave_publica_a = rsa.PublicKey.load_pkcs1(chave_publica_a_pem.encode())

# === Mensagem criptografada (Base64) ===
mensagem_criptografada_b64 = """
UNfG91DrZw1MkYdPD2YyG/gu2cf1rEbSbfV+D20XLZ9DHs2MWNRDO5H7g6+APd6M/zqUEnvXE6MgmGCO5iOStOwTt6Lger2OOLtgbLa87S24DiUXC2SvnSf6T/AKk8hAUeQYG1EGv+f+clK2Jd7Goz93uMASZ8dg8bNshvCUZagB6JXAGiQDmQ1DlCYJre+ScmupUGskpopUfoB2imudYqgAHJLXMs3t+nI/46KUgEZ5PrOb5/2yafrJ+om4NgupxyX+fcrBjaa+vtNEohYz/bg99BngubXDPIbPXt8mAPGSLQG7dCDWx1NvhIsecRC15rT7NFIg/MOc/LGdXD4P5g==
""".strip()

# === Assinatura digital (Base64) ===
assinatura_b64 = """
EpHEwI/ZGCKvzFeh6PvEKiH5y5MoCAld9qrizoL6EWMM9w/FJWhRdux53Fq64EY6uLMQHaX9mXHyJ1X//Ck12w==
""".strip()

# === Decodificar os dados Base64 ===
mensagem_criptografada = base64.b64decode(mensagem_criptografada_b64)
assinatura = base64.b64decode(assinatura_b64)

# === Descriptografar mensagem ===
try:
    mensagem_original = rsa.decrypt(mensagem_criptografada, chave_privada_b)
    print("🔓 Mensagem descriptografada com sucesso:")
    print(mensagem_original.decode())
except Exception as e:
    print("❌ Erro ao descriptografar:", e)
    exit()

# === Verificar assinatura ===
try:
    rsa.verify(mensagem_original, assinatura, chave_publica_a)
    print("✅ Assinatura VÁLIDA: a mensagem é autêntica e não foi modificada.")
except rsa.VerificationError:
    print("❌ Assinatura INVÁLIDA: a mensagem foi modificada ou a assinatura não é da Equipe A.")
