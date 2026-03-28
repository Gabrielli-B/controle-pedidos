import funcionalidades
import manipulacaoBanco

vcon=manipulacaoBanco.ConexaoBanco()

vsql = """CREATE TABLE IF NOT EXISTS tb_produtos(
            ID_PRODUTO  INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME_PRODUTO VARCHAR(30),
            PRECO_PRODUTO FLOAT,
            ESTOQUE_PRODUTO INT
        );"""

vsql2 = """CREATE TABLE IF NOT EXISTS tb_pedidos(
            ID_PEDIDO INTEGER PRIMARY KEY AUTOINCREMENT,
            DATA_PEDIDO DATE,
            VALORTOTAL_PEDIDO FLOAT
        );"""

manipulacaoBanco.query(vcon,vsql)
manipulacaoBanco.query(vcon,vsql2)
manipulacaoBanco.vcon.close()


def menu():
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Atualizar  Produto")
    print("4 - Remover  Produto")
    print("5 - Novo Pedido")
    print("6 - Ver Pedidos")
    print("7 - Relatórios")
    print("8 - Sair")

op=0

while(op != 8):
    menu()
    op=int(input("Escolha uma opção: "))

    if(op == 1):
        nome=input("Informe o nome do produto: ")
        preco=float(input("Informe o preço do produto: "))
        estoque=int(input("Informe a quantidade de estoque: "))
        produto = funcionalidades.cadastrarProduto(nome,preco,estoque)
        