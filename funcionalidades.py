import produto
import validacoes
from pedidos import Pedidos
from itensPedido import ItensPedido
from datetime import date

def cadastrarProduto(nome, preco,estoque):
    validacoes.validarEstoquePreco(preco,estoque)
    novoProduto = produto.Produto(nome,preco,estoque)
    return novoProduto

def cadastrarPedido(lista_itens):
    pedido = Pedidos(str(date.today()))

    for item in lista_itens:
        pedido.adicionarItem(item)

    return pedido

##def consultarRegistroExiste():

