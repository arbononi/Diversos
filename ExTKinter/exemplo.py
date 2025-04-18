import tkinter as tk
from tkinter import messagebox

def salvar():
    cpf = cpf_entry.get()
    nome = nome_entry.get()
    data_nasc = data_entry.get()
    messagebox.showinfo("Cadastro", f"CPF: {cpf}\nNome: {nome}\nData de nascimento: {data_nasc}")

root = tk.Tk()
root.title("Cadastro de Paciente")

tk.Label(root, text="CPF:").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Nome:").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Data de nascimento:").grid(row=2, column=0, sticky="e")

cpf_entry = tk.Entry(root)
nome_entry = tk.Entry(root)
data_entry = tk.Entry(root)

cpf_entry.grid(row=0, column=1)
nome_entry.grid(row=1, column=1)
data_entry.grid(row=2, column=1)

tk.Button(root, text="Salvar", command=salvar).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
