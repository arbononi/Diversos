def mostrar_tabela_cores():
    for i in range(0, 256):
        # Imprime o número da cor com fundo colorido e texto centralizado
        print(f"\033[48;5;{i}m\033[38;5;15m {i:>3} \033[0m", end=' ')
        if (i + 1) % 16 == 0:
            print()  # Nova linha a cada 16 cores

def mostrar_tabela_cores_texto():
    for i in range(0, 256):
        # Cor do texto com fundo preto (background 0), número visível
        print(f"\033[48;5;0m\033[38;5;{i}m {i:>3} \033[0m", end=' ')
        if (i + 1) % 16 == 0:
            print()  # Nova linha a cada 16 cores


if __name__ == "__main__":
    mostrar_tabela_cores()
    print()
    mostrar_tabela_cores_texto()
