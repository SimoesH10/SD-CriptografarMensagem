# Equipe B - Gerar Chaves RSA
import rsa
import os

os.makedirs("chaves", exist_ok=True)

public_key, private_key = rsa.newkeys(2048)

with open("chaves/chave_publica_b.pem", "wb") as pub:
    pub.write(public_key.save_pkcs1("PEM"))

with open("chaves/chave_privada_b.pem", "wb") as priv:
    priv.write(private_key.save_pkcs1("PEM"))

print("Chaves da Equipe B geradas com sucesso.")
