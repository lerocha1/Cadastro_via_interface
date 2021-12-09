import tkinter as tk
import sqlite3
from funcoes_def import  exporta_clientes, abrir_janela
import pandas as pd

# #Criando o Banco de Dados: ATé linha 30 roda apenas 1 vez!
#
conexao = sqlite3.connect('clientes.db')
#
#Criando Cursor
c = conexao.cursor()

#criando a tabela
c.execute("""
            create table if not exists clientes (
            nome text,
            sobrenome text,
            email text,
            telefone text,
            data_nasc date)
            """)

#commit nas mudanças
conexao.commit()

#fechar o banco de dados:

conexao.close()

def abrir_janela2():
    janela2 = tk.Toplevel()
    janela2.title('Janela nova!!')
    janela2.geometry("150x100")
    label_nome = tk.Label(janela2, text = 'Nome')
    label_nome.grid(row = 0, column = 0)
    botao_voltar = tk.Button(janela2, text='Fechar Janela nova', command = janela2.destroy)
    botao_voltar.grid(row=1, column = 0)

def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:email,:telefone, :data_nasc)",
              {
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get(),
                  'data_nasc':entry_data_nasc.get()
              })


    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_email.delete(0,"end")
    entry_telefone.delete(0,"end")
    entry_data_nasc.delete(0, 'end')


#Criando Janela:

janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela. geometry("390x350")


#Rótulos Entradas:
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0 , padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

label_data_nasc = tk.Label(janela, text='Data de Nascimento')
label_data_nasc.grid(row=4, column=0, padx=10, pady=10)

#Caixas Entradas:
entry_nome = tk.Entry(janela , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width =35)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width =35)
entry_email.grid(row=2, column=1 , padx=10, pady=10)

entry_telefone = tk.Entry(janela, width =35)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

entry_data_nasc = tk.Entry(janela, width =35)
entry_data_nasc.grid(row=4, column=1, padx=10, pady=10)



# Botão de Cadastrar

botao_cadastrar = tk.Button(janela,text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=5, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Exportar

botao_exportar = tk.Button(janela,text='Exportar para Excel', command=exporta_clientes)
botao_exportar.grid( row=6, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Nova Janela

botao_nova_janela = tk.Button(text='Abrir Nova Janela', command=abrir_janela)
botao_nova_janela.grid(row=7, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)


janela.mainloop()


