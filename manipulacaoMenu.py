import manipulacaoBanco
import tabelasBanco
import funcionalidades
from itensPedido import ItensPedido

vcon=manipulacaoBanco.ConexaoBanco()


manipulacaoBanco.query(vcon,tabelasBanco.vsql)
manipulacaoBanco.query(vcon,tabelasBanco.vsql2)
manipulacaoBanco.query(vcon,tabelasBanco.vsql3)


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

def menuNovoPedido():
    lista_itens = []

    while True :
        op=int(input(" 1 - Adicionar item ao pedido\n  2 - sair\nEscolha: "))

        if op == 2:
            break

        try:
            idProduto = int(input("Informe o ID do produto: "))
            produto = funcionalidades.consultarRegistroExiste(vcon,idProduto)
            qtd = int(input("Informe a quantidade: "))

            preco = produto[2]
            estoque = produto[3]

            if qtd > estoque:
                print("Estoque insuficiente!")
                continue
            item = ItensPedido(idProduto,preco,qtd)
            lista_itens.append(item)
            print("Item adicionado!")
        except Exception as e:
            print(e)

    if len(lista_itens) == 0 :
        print("Pedido Vazio!")
        return
    funcionalidades.salvarPedido(vcon,lista_itens)

def menuVerPedidos():
    vsql="SELECT * FROM tb_pedidos"
    res=manipulacaoBanco.consultar(vcon,vsql)
    for r in res:
        print(f"ID:{r[0]}")
        print(f"Data Pedido:{r[1]}")
        print(f"Valor total pedido:{r[2]}")

vcon.close()