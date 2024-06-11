import os
import pyaes

def decrypt_file(file_path, key):
    try:
        # Abrir o arquivo criptografado
        with open(file_path, "rb") as file:
            # Ler os dados criptografados
            crypto_data = file.read()

        # Instanciar o AES com a chave
        aes = pyaes.AESModeOfOperationCTR(key)

        # Descriptografar os dados do arquivo
        file_data = aes.decrypt(crypto_data)

        # Recuperar o caminho do arquivo original
        original_file_path = file_path.replace(".encrypted", "")

        # Salvar os dados descriptografados no arquivo original
        with open(original_file_path, "wb") as new_file:
            new_file.write(file_data)

        # Remover o arquivo criptografado
        os.remove(file_path)

        print(f"Arquivo {file_path} desencriptado com sucesso!")

    except Exception as e:
        print(f"Erro ao desencriptar o arquivo {file_path}: {e}")

def decrypt_directory(directory, key):
    # Verificar se o diretório existe
    if not os.path.isdir(directory):
        print(f"Erro: O diretório {directory} não existe.")
        return

    try:
        # Percorrer todos os arquivos no diretório
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".encrypted"):
                    file_path = os.path.join(root, file)
                    decrypt_file(file_path, key)

        print("Tudo certo agora!")

    except Exception as e:
        print(f"Erro ao desencriptar o diretório {directory}: {e}")

if __name__ == "__main__":
    # Definir a chave de descriptografia (deve ser a mesma usada na criptografia)
    key = b"testeransomwares"

    # Diretório a ser desencriptado
    directory = "caminho/para/a/pasta"

    # Chamar a função para desencriptar o diretório
    decrypt_directory(directory, key)
