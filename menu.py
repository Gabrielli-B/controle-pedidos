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


def menu():
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Atualizar  Produto")
    print("4 - Remover  Produto")
    print("5 - Novo Pedido")
    print("6 - Ver Pedidos")
    print("7 - Relatórios")
    print("8 - Sair")

def menuInserir():
    nome=input("Informe o nome do produto: ")
    preco=float(input("Informe o preço do produto: "))
    estoque=int(input("Informe a quantidade de estoque: "))
    produto = funcionalidades.cadastrarProduto(nome,preco,estoque)
    vsql = "INSERT INTO tb_produtos(NOME_PRODUTO, PRECO_PRODUTO, ESTOQUE_PRODUTO) VALUES (?,?,?)"
    dados=(produto.nome,produto.preco,produto.estoque)
    manipulacaoBanco.query(vcon,vsql,dados)

def menuListar():
    vsql="SELECT * FROM tb_produtos"
    res=manipulacaoBanco.consultar(vcon,vsql)
    for r in res:
        print("ID:{r[0]}")
        print("Nome:{r[1]}")
        print("Preço R$:{r[2]}")
        print("Estoque:{r[3]}")
        print("-" *30)


def menuAtualizar():
    vid=int(input("Digite o ID do registro a ser Atualizado:"))
    r=manipulacaoBanco.consultar(vcon,"SELECT * FROM tb_produtos WHERE ID_PRODUTO="+vid)
    rnome=r[0][1]
    rpreco=r[0][2]
    restoque=r[0][3]

    vnome=input("Digite o nome do produto:")
    vpreco=float(input("Informe o preço do produto:"))
    vestoque=int(input("Informe o estoque:"))

    if(len(vnome)==0):
        vnome=rnome
    if(len(vpreco)==0):
        vpreco=rpreco
    if(len(vestoque)==0):
        vestoque=restoque

    vsql="UPDATE tb_produtos SET NOME_PRODUTO='"+vnome+"', PRECO_PRODUTO'"+vpreco+"', ESTOQUE_PRODUTO'"+vestoque+"'"
    manipulacaoBanco.query(vcon,vsql)

op=0

while(op != 8):
    menu()
    op=int(input("Escolha uma opção: "))

    if(op == 1):
       menuInserir()
    elif(op==2):
        menuListar()
    elif(op==3):
        menuAtualizar()

vcon.close()       