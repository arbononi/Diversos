import time
import os
import sys

TOP = 4
BOTTOM = 28
HEIGHT = BOTTOM - TOP - 1
WIDTH = 70

log_buffer = []  # Armazena as linhas do "quadro"

def clear_terminal():
    print("\033[2J\033[H", end='')  # limpa a tela e vai para o topo

def move_cursor(x, y):
    print(f"\033[{y};{x}H", end='')

def draw_frame():
    move_cursor(1, TOP)
    print("╔" + "═" * WIDTH + "╗")
    for y in range(TOP + 1, BOTTOM):
        move_cursor(1, y)
        print("║" + " " * WIDTH + "║")
    move_cursor(1, BOTTOM)
    print("╚" + "═" * WIDTH + "╝")

def write_line(text):
    if len(log_buffer) >= HEIGHT:
        log_buffer.pop(0)  # remove a linha mais antiga
    log_buffer.append(text)

    # reescreve todo o conteúdo visível
    for i, line in enumerate(log_buffer):
        move_cursor(2, TOP + 1 + i)
        print(line.ljust(WIDTH)[:WIDTH], end='')

    sys.stdout.flush()

# Exemplo de uso
if __name__ == "__main__":
    clear_terminal()
    draw_frame()

    for i in range(40):
        write_line(f"Texto da linha {i+1}")
        time.sleep(0.2)
