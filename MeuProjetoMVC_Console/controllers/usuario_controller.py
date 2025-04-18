from models.usuario import Usuario
from views.usuario_view import menu_principal, solicitar_dados_usuario, mostrar_usuarios

class UsuarioController:
    def __init__(self):
        self.usuarios = []

    def iniciar(self):
        while True:
            opcao = menu_principal()

            if opcao == "1":
                nome, email = solicitar_dados_usuario()
                usuario = Usuario(nome, email)
                self.usuarios.append(usuario)
                print("Usuário cadastrado com sucesso!")

            elif opcao == "2":
                mostrar_usuarios(self.usuarios)

            elif opcao == "3":
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida. Tente novamente.")
