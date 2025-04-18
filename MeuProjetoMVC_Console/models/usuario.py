class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}"