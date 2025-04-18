def menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Sair")
    return input("Escolha uma opção: ")

def solicitar_dados_usuario():
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    return nome, email

def mostrar_usuarios(usuarios):
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario}")
