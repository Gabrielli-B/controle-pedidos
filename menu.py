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

vsql3= """CREATE TABLE IF NOT EXISTS tb_itenspedido(
            ID_ITEM INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_PRODUTO INTEGER,
            ID_PEDIDO  INTEGER,
            QTD_ITEMPEDIDO INTEGER,
            SUBTOTAL_ITEMPEDIDO REAL,

            FOREIGN KEY(ID_PRODUTO)
                REFERENCES tb_produtos(ID_PRODUTO)

            FOREIGN KEY(ID_PEDIDO)
                REFERENCES tb_pedidos(ID_PEDIDO)
            
        );"""

manipulacaoBanco.query(vcon,vsql)
manipulacaoBanco.query(vcon,vsql2)
manipulacaoBanco.query(vcon,vsql3)


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
        print(f"ID:{r[0]}")
        print(f"Nome:{r[1]}")
        print(f"Preço R$:{r[2]}")
        print(f"Estoque:{r[3]}")
        print("-" *30)


def menuAtualizar():
    vid=int(input("Digite o ID do registro a ser Atualizado:"))
    vsql="SELECT *FROM tb_produtos WHERE ID_PRODUTO=?"
    r=manipulacaoBanco.consultar(vcon,vsql,(vid,))

    if len(r)==0:
        print("Produto não encontrado!")
        return
    
    rnome=r[0][1]
    rpreco=r[0][2]
    restoque=r[0][3]

    vnome=input("Digite o nome do produto:")
    vpreco=input("Informe o preço do produto:")
    vestoque=input("Informe o estoque:")

    if vnome =="":
        vnome=rnome
    if vpreco =="":
        vpreco=rpreco
    else:
        vpreco=float(vpreco)
    
    if vestoque=="":
       vestoque=restoque
    else:
        vestoque=int(vestoque)

    vsql="UPDATE tb_produtos SET NOME_PRODUTO=?, PRECO_PRODUTO=?, ESTOQUE_PRODUTO=? WHERE ID_PRODUTO=?"

    dados=(vnome,vpreco,vestoque,vid)
    manipulacaoBanco.query(vcon,vsql,dados)
    

def menuRemover():
    vid=int(input("Digite o ID do registro a ser deletado: "))
    vsql="DELETE FROM tb_produtos WHERE ID_PRODUTO =?"
    manipulacaoBanco.query(vcon,vsql,(vid,))
    print("Produto removido!")

#def menuNovoPedido():


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
    elif(op==4):
        menuRemover()
#    elif(op==5):
 #       menuNovoPedido()

vcon.close()