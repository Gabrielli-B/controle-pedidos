import excecao

def validarEstoquePreco(num1,num2):
    if(num1 < 0 or num2 < 0):
        raise excecao.EstoquePrecoInvalidoError("Estoque ou preço do produto não podem ser negativos")