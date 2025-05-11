import os
import shutil
import time

# ANSI para posicionamento e estilo
def move_cursor(y, x):
    print(f"\033[{y};{x}H", end='')

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class WindowManager:
    def __init__(self):
        self.stack = []
        self.width, self.height = shutil.get_terminal_size()
        self.saved_screen = []

    def save_background(self, x, y, w, h):
        bg = []
        for i in range(h):
            move_cursor(y + i, x)
            line = input()  # Para leitura real seria necessário manipulação mais baixa
            bg.append((y + i, x, line))
        return bg

    def draw_box(self, x, y, w, h, message):
        lines = []
        lines.append("╔" + "═" * (w - 2) + "╗")
        for _ in range(h - 2):
            lines.append("║" + " " * (w - 2) + "║")
        lines.append("╚" + "═" * (w - 2) + "╝")

        for i, line in enumerate(lines):
            move_cursor(y + i, x)
            print(line, end="")

        move_cursor(y + h // 2, x + 2)
        print(message[:w - 4], end="")

        move_cursor(y + h - 2, x + 2)
        print("Pressione ENTER para continuar...", end="")

        # Salva para empilhar
        self.stack.append((x, y, w, h, lines))

    def close_top(self):
        if not self.stack:
            return

        x, y, w, h, _ = self.stack.pop()
        for i in range(h):
            move_cursor(y + i, x)
            print(" " * w, end="")

    def run_demo(self):
        clear_screen()
        print("Conteúdo original da tela")
        print("Texto importante que será encoberto.")
        input("Pressione ENTER para abrir janela...")

        self.draw_box(10, 5, 50, 7, "Janela 1")
        print()
        input()
        self.close_top()

        input("Pressione ENTER para abrir outra...")
        self.draw_box(20, 8, 40, 6, "Janela 2")
        input()
        self.close_top()

        move_cursor(self.height, 0)
        print("Fim da demonstração.")

if __name__ == "__main__":
    wm = WindowManager()
    wm.run_demo()
