import tkinter as tk
from tkinter import messagebox
import subprocess


def fazer_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "usuario" and password == "senha":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        subprocess.call(["python3", "main.py"])
    else:
        messagebox.showerror("Login", "Credenciais inválidas.")

# Criação da janela
janela = tk.Tk()
janela.title("Tela de Login")

# Definir a resolução e centralizar a janela
largura = 1360
altura = 720
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{x}+{y}")

label_username = tk.Label(janela, text="Usuário:")
label_username.pack()

entry_username = tk.Entry(janela)
entry_username.pack()

label_password = tk.Label(janela, text="Senha:")
label_password.pack()

# Campo de entrada de senha
entry_password = tk.Entry(janela, show="*")
entry_password.pack()

# Botão de login
button_login = tk.Button(janela, text="Login", command=fazer_login)
button_login.pack()

# Execução da janela
janela.mainloop()
