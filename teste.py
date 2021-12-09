import tkinter as tk
import sqlite3
import pandas as pd
from funcoes_def import visualiza_clientes

def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    for x in range(9): # 0 is unnecessary
        label = tk.Label(janela2, text= str(x))
    # this creates x as a new label to the GUI
        label.pack()

def print():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome', 'email', 'telefone', 'data_nasc', 'Id_banco'])
    # Commit as mudanças:
    conexao.commit()
    label = tk.Label(janela2, text=str(clientes_cadastrados.head()))
    label.pack
    # Fechar o banco de dados:
    conexao.close()

def print_facil():

    label = tk.Label(janela2, text="""Murilo Lindo 
     Samuca Tesão
     SEA ainda existe!!
    """ )

    # this creates x as a new label to the GUI
    label.pack()


janela2 = tk.Tk()
janela2.geometry("200x150")

button = tk.Button(janela2, text="Print Me", command=print_facil)
button.pack()

janela2.mainloop()
