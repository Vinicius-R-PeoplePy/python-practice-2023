import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute('''
        create table agenda(
            nome text,
               telefone text)
        ''')
cursor.execute('''
        insert into agenda(nome, telefone)
            values(?, ?)
            ''', ("Nilo", "7788-1432"))
conexão.commit()
cursor.close()
conexão.close 

import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
resultado=cursor.fetchone()
print("Nome: %s\nTelefone: %s" % (resultado))
cursor.close()
conexão.close()

import sqlite3 
dados = [ ("João", "98901-0109"),
         ("André", "98902-8900"),
         ("Maria", "97891-3321")]
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.executemany('''
        insert into agenda (nome, telefone)
        values(?, ?)
        ''', dados)
conexão.commit()
cursor.close()
conexão.close()

import sqlite3 
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
resultado=cursor.fetchall()
for registro in resultado:
    print("Nome: %s\nTelefone: %s" % (registro))
cursor.close()
conexão.close()

# consulta, registro por registro 
import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
while True:
    resultado=cursor.fetchone()
    if resultado == None:
        break 
    print("Nome: %s\nTelefone: %s" % resultado)
cursor.close()
conexão.close 

# uso do with para fechar a conexão

import sqlite3 
from contextlib import closing

with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("select * from agenda")
        while True:
            resultado=cursor.fetchone()
            if resultado == None:
                break 
            print("Nome: %s\nTelefone: %s" % (resultado))

    