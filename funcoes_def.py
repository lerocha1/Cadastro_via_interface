import sqlite3
import pandas as pd
import tkinter as tk


def exporta_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['nome','sobrenome','email','telefone','data_nasc','Id_banco'])
    clientes_cadastrados.to_excel('clientes.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()


def abrir_janela():
    janela2 = tk.Toplevel()
    janela2.title('Janela nova!!')
    janela2.geometry("150x100")
    label_nome = tk.Label(janela2, text = 'Nome')
    label_nome.grid(row = 0, column = 0)
    botao_voltar = tk.Button(janela2, text='Fechar Janela nova', command = janela2.destroy)
    botao_voltar.grid(row=1, column = 0)

def visualiza_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['nome','sobrenome','email','telefone','data_nasc','Id_banco'])

    # Commit as mudanças:
    conexao.commit()

    label = tk.Label(janela3, text=str(clientes_cadastrados))

    # Fechar o banco de dados:
    conexao.close()