import os
import pyaes

# Lista de extensões que o ransomware pode usar
extensions = ['.ransoware', '.locked', '.encrypted', '.crypt', '.enc']  # Adicione outras extensões se necessário

# Procurar o arquivo a ser descriptografado
file_name = None
for ext in extensions:
    possible_file = f'arquivo{ext}'  # Substitua 'arquivo' pelo prefixo base do arquivo
    if os.path.exists(possible_file):
        file_name = possible_file
        break

if file_name is None:
    raise FileNotFoundError("Nenhum arquivo criptografado encontrado com as extensões fornecidas.")

# Abrir o arquivo criptografado
with open(file_name, 'rb') as file:
    file_data = file.read()

# Chave de descriptografia
key = b'testeransoware'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo original
os.remove(file_name)

# Salvar o arquivo descriptografado
new_file = file_name + '.txt'  # Substitua conforme necessário
with open(new_file, 'wb') as file:
    file.write(decrypt_data)

print(f"Arquivo descriptografado salvo como: {new_file}")
