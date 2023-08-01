**README - Criptografia e Descriptografia com PyAES**

Este é um projeto simples em Python, desenvolvido durante um curso da Plataforma da DIO que demonstra como criptografar e descriptografar um arquivo usando o módulo `pyaes`. O objetivo deste código é apenas educacional, e não deve ser usado para fins maliciosos ou ilegais.

**Como funciona o código de criptografia:**

1. **Abertura do arquivo a ser criptografado:**
   - O código começa definindo o nome do arquivo que será criptografado, neste caso, "teste.txt".
   - O arquivo é aberto em modo leitura binária ("rb") para obter o conteúdo em bytes e armazenado na variável `file_data`.

2. **Remoção do arquivo original:**
   - Após ler o conteúdo do arquivo, o código utiliza a biblioteca `os` para remover o arquivo original "teste.txt" do sistema.

3. **Chave de criptografia:**
   - Uma chave é definida para criptografar o arquivo. Neste exemplo, a chave é "testeransomwares" representada em bytes.

4. **Criptografia do arquivo:**
   - O algoritmo AES no modo CTR é usado para criptografar os dados do arquivo. A biblioteca `pyaes` é utilizada para realizar a criptografia.
   - Os dados criptografados são armazenados na variável `crypto_data`.

5. **Salvando o arquivo criptografado:**
   - O código cria um novo nome de arquivo com a extensão ".ransomwaretroll", resultando em "teste.txt.ransomwaretroll".
   - O arquivo criptografado é então salvo com esse novo nome e o conteúdo criptografado.



**Como funciona o código de descriptografia:**

1. **Abertura do arquivo criptografado:**
   - O código define o nome do arquivo criptografado que será descriptografado, neste caso, "teste.txt.ransomwaretroll".
   - O arquivo é aberto em modo leitura binária ("rb") para obter o conteúdo em bytes e armazenado na variável `file_data`.

2. **Chave para descriptografia:**
   - A mesma chave utilizada para criptografar o arquivo ("testeransomwares") é usada para a descriptografia.

3. **Descriptografia do arquivo:**
   - O algoritmo AES no modo CTR é novamente usado para descriptografar os dados do arquivo.
   - Os dados descriptografados são armazenados na variável `decrypt_data`.

4. **Remoção do arquivo criptografado:**
   - Após a descriptografia, o código utiliza a biblioteca `os` para remover o arquivo criptografado "teste.txt.ransomwaretroll" do sistema.

5. **Criação do arquivo descriptografado:**
   - O código cria um novo arquivo chamado "teste.txt".
   - O conteúdo descriptografado é salvo nesse novo arquivo.

**Observação:**
- Lembre-se de que a chave usada neste código é apenas uma chave de exemplo e não é segura para uso real. Em um cenário real, é fundamental utilizar uma chave forte e segura, bem como implementar práticas adequadas de gerenciamento de chaves.
- O código aqui apresentado é apenas um exemplo educacional de como usar a biblioteca `pyaes` para criptografar e descriptografar arquivos. Para criptografia e segurança real, recomenda-se o uso de bibliotecas de criptografia bem estabelecidas e seguras, além de seguir as melhores práticas de segurança.

