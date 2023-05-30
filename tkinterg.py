import tkinter as tk
from tkinter import messagebox
from sql_queries import Database

class CRUDApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("CRUD")
        self.database = Database("meu_banco.db")
        self.registros = self.database.read()


        self.criar_interface()

    def criar_interface(self):
        self.configurar_janela()
        self.criar_campos()
        self.criar_botoes()
        self.criar_listbox()
        self.exibir_registros()

    def configurar_janela(self):
        largura_janela = 1360
        altura_janela = 720
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        posicao_x = int(largura_tela/2 - largura_janela/2)
        posicao_y = int(altura_tela/2 - altura_janela/2)
        self.janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        self.janela.configure(bg="#F2F2F2")

    def criar_campos(self):
        self.id_label = tk.Label(
            self.janela,
            text="Id:",
            font=("Arial", 12),
            bg="#F2F2F2"
        )
        self.id_label.place(relx=0.25, rely=0.1, anchor=tk.CENTER)

        self.id_entry = tk.Entry(
            self.janela,
            font=("Arial", 12)
        )
        self.id_entry.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.produto_label = tk.Label(
            self.janela,
            text="produto:",
            font=("Arial", 12),
            bg="#F2F2F2"
        )
        self.produto_label.place(relx=0.25, rely=0.2, anchor=tk.CENTER)

        self.produto_entry = tk.Entry(
            self.janela,
            font=("Arial", 12)
        )
        self.produto_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.preco_label = tk.Label(
            self.janela,
            text="preco:",
            font=("Arial", 12),
            bg="#F2F2F2"
        )
        self.preco_label.place(relx=0.25, rely=0.3, anchor=tk.CENTER)

        self.preco_entry = tk.Entry(
            self.janela,
            font=("Arial", 12)
        )
        self.preco_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    def criar_botoes(self):
        self.adicionar_button = tk.Button(
            self.janela,
            text="Adicionar",
            command=self.adicionar_registro,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white"
        )
        self.adicionar_button.place(relx=0.25, rely=0.4, anchor=tk.CENTER)

        self.editar_button = tk.Button(
            self.janela,
            text="Editar",
            command=self.editar_registro,
            font=("Arial", 12),
            bg="#FF9800",
            fg="white"
        )
        self.editar_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.apagar_button = tk.Button(
            self.janela,
            text="Apagar",
            command=self.apagar_registro,
            font=("Arial", 12),
            bg="#F44336",
            fg="white"
        )
        self.apagar_button.place(relx=0.75, rely=0.4, anchor=tk.CENTER)

    def criar_listbox(self):
        self.registros_listbox = tk.Listbox(
            self.janela,
            font=("Arial", 12),
            width=60,
            height=10
        )
        self.registros_listbox.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def adicionar_registro(self):
        id = self.id_entry.get()
        produto = self.produto_entry.get()
        preco = self.preco_entry.get()

        ids = [id[0] for id in self.database.read()]

        if id in ids:
            messagebox.showerror("Error", "Já existe usuario com essa id")
            self.limpar_campos()
            self.exibir_registros()

        if id and produto and preco:
            self.database.create(id, produto, preco)
            messagebox.showinfo("Sucesso", "Registro adicionado com sucesso!")
            self.limpar_campos()
            self.exibir_registros()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def editar_registro(self):
        selecionado = self.registros_listbox.curselection()
        if len(selecionado) == 0:
            messagebox.showerror("Erro", "Nenhum registro selecionado.")
            return

        id = self.id_entry.get()
        produto = self.produto_entry.get()
        preco = self.preco_entry.get()

        if id and produto and preco:
            self.database.update(id, produto, preco)
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
            self.limpar_campos()
            self.exibir_registros()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def apagar_registro(self):
        selecionado = self.registros_listbox.curselection()
        if len(selecionado) == 0:
            messagebox.showerror("Erro", "Nenhum registro selecionado.")
            return

        indice = selecionado[0]
        registro = self.registros[indice]
        id = registro[0]

        self.database.delete(id)
        messagebox.showinfo("Sucesso", "Registro apagado com sucesso!")
        self.limpar_campos()
        self.exibir_registros()

    def limpar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.produto_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)

    def exibir_registros(self):
        self.registros_listbox.delete(0, tk.END)
        self.registros = self.database.read()

        for registro in self.registros:
            id, produto, preco = registro
            self.registros_listbox.insert(tk.END, f"Id: {id}, produto: {produto}, preco: {preco}")
