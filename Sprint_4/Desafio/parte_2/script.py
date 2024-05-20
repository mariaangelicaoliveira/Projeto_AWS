import hashlib

def main():
    while True:
        # Recebe uma string via input
        input_string = input("Digite uma string (ou 'sair' para encerrar): ")

        # Verifica se o usuário deseja sair do loop
        if input_string.lower() == 'sair':
            print("Encerrando o programa.")
            break

        # Gera o hash da string usando o algoritmo SHA-1
        hash_object = hashlib.sha1(input_string.encode())
        hash_hex = hash_object.hexdigest()

        # Imprime o hash em tela utilizando o método hexdigest
        print(f"O hash SHA-1 da string '{input_string}' é: {hash_hex}")

if __name__ == "__main__":
    main()
