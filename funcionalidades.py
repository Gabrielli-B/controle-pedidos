import produto
import validacoes

def cadastrarProduto(nome, preco,estoque):
    validacoes.validarEstoquePreco(preco,estoque)
    novoProduto = produto.Produto(nome,preco,estoque)
    return novoProduto

