import os
import pyaes

# ABRINDO O ARUIVO CRIPTO
file_name = "teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# CHAVE PRA DESCRIPTOGRAFAR
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# REMOVE O ARQUIVO CRIPTOGRAFADO
os.remove(file_name)

# CRIA UM ARQUIVO DESCRIPTOGRAFADO
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
