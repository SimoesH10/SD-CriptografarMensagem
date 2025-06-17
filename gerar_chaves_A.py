# Gerar a chave A
import rsa
import os

# Criar diretório "chaves" se não existir
os.makedirs("chaves", exist_ok=True)

# Gerar par de chaves RSA (2048 bits)
public_key, private_key = rsa.newkeys(2048)

# Salvar chave pública no formato PEM (.pem)
with open("chaves/chave_publica_a.pem", "wb") as pub_pem:
    pub_pem.write(public_key.save_pkcs1("PEM"))

# Salvar chave privada no formato PEM (.pem)
with open("chaves/chave_privada_a.pem", "wb") as priv_pem:
    priv_pem.write(private_key.save_pkcs1("PEM"))

# Salvar chave pública no formato texto (.txt)
with open("chaves/chave_publica_a.txt", "w") as pub_txt:
    pub_txt.write(public_key.save_pkcs1("PEM").decode())

# Salvar chave privada no formato texto (.txt)
with open("chaves/chave_privada_a.txt", "w") as priv_txt:
    priv_txt.write(private_key.save_pkcs1("PEM").decode())

print("Chaves da Equipe A geradas e salvas com sucesso nos formatos .pem e .txt.")
