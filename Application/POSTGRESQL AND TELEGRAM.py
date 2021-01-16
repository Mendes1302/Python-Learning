import psycopg2 as sql
import sys
import numpy as np

global vetor
vetor = np.empty([0], dtype=int)

con = sql.connect(database='teste', user='postgres', password='1302')
cur = con.cursor()

def update_matriz():
    global vetor
    cur.execute(f'SELECT id_chat from controle')
    for table in cur.fetchall():
        vetor = np.append(vetor, table)
    return vetor

def inserir(chat_id, CPF):
    try:
        cur.execute('INSERT INTO controle (id_chat, CPF) VALUES (%s, %s)', (chat_id, CPF))
        con.commit()
    except Exception as erro:
        print(f'Error {erro}')
        sys.exit(1)

def update(chat_id, CPF):
    try:
        cur.execute(f'UPDATE controle set CPF = {CPF} where id_chat = {chat_id}')
        con.commit()

    except Exception as erro:
        print(f'Error {erro}')
        sys.exit(1)

def delete(CPF, chat_id):
    try:
        cur.execute(f'DELETE FROM controle where CPF = {CPF} and id_chat = {chat_id}')
        con.commit()

    except Exception as erro:
        print(f'Error {erro}')
        sys.exit(1)

try:
    escolha = str(input("Digite o que quer fazer:\ninserir\nupdate\ndelete\n")).upper()

    if escolha in 'INSERIR':
        chat = int(input("Digite o valor do chat_id: "))
        CPF = int(input("Digite o CPF de um cliente: "))
        inserir(chat, CPF)
    elif escolha in 'UPDATE':
        chat = int(input("Digite o valor do chat_id: "))
        CPF = int(input("Digite o novo CPF: "))
        update(chat, CPF)
    elif escolha in 'DELETE':
        chat = int(input("Digite o chat_id a remover: "))
        CPF = int(input("Digite o CPF a remover: "))
        delete(CPF, chat)
    #update_matrix no BD
    update_matriz()

    cur.execute(f'SELECT * from controle')
    for table in cur.fetchall():
        print(table)

except Exception as erro:
    print(f'Error {erro}')
    sys.exit(1)
