import sqlite3 
from sqlite3 import Error

def ConexaoBanco():
    caminho = "controle_pedidos.db"
    con = None
    try :
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

def query(conexao,sql,dados=None):
    try:
        c = conexao.cursor()
        if dados is not None:
            c.execute(sql,dados)
        else:
            c.execute(sql)  
        conexao.commit()
    except Error as ex:
        print(ex)

def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    return res
