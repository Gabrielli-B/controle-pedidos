import produto
import validacoes
from pedidos import Pedidos
from datetime import date
from manipulacaoBanco import consultar, query
from excecao import IDNaoExisteError

def cadastrarProduto(nome, preco,estoque):
    validacoes.validarEstoquePreco(preco,estoque)
    novoProduto = produto.Produto(nome,preco,estoque)
    return novoProduto

def cadastrarPedido(lista_itens):
    pedido = Pedidos(str(date.today()))

    for item in lista_itens:
        pedido.adicionarItem(item)

    return pedido

def consultarRegistroExiste(vcon, id):
    vsql = "SELECT * FROM tb_produtos WHERE ID_PRODUTO=?"
    res =  consultar(vcon,vsql,(id,))

    if len(res) == 0:
        raise IDNaoExisteError("Id não existe!")

    return res[0]

def salvarPedido(vcon, lista_itens):
    from datetime import date

    data = str(date.today())
    valorTotal = sum(item.subtotal for item in lista_itens)


    vsql = "INSERT INTO tb_pedidos(DATA_PEDIDO, VALORTOTAL_PEDIDO) VALUES (?,?)"
    query(vcon, vsql, (data, valorTotal))


    idPedido = consultar(vcon, "SELECT last_insert_rowid()")[0][0]

    for item in lista_itens:
        vsqlItem = """
        INSERT INTO tb_itenspedido 
        (ID_PRODUTO, ID_PEDIDO, QTD_ITEMPEDIDO, SUBTOTAL_ITEMPEDIDO)
        VALUES (?,?,?,?)
        """
        dados = (item.id_produto, idPedido, item.qtd, item.subtotal)
        query(vcon, vsqlItem, dados)

        # baixa estoque
        vsqlEstoque = """
        UPDATE tb_produtos 
        SET ESTOQUE_PRODUTO = ESTOQUE_PRODUTO - ?
        WHERE ID_PRODUTO = ?
        """
        query(vcon, vsqlEstoque, (item.qtd, item.id_produto))

    print(f"Pedido {idPedido} criado com sucesso!")
