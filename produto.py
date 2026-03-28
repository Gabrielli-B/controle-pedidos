
class Produto:
    def __init__(self, nome, preco, estoque, idProduto=None):
        self.idProduto = idProduto
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibirDetalhes(self):
        print("Nome............ " + self.nome)
        print("Preço........... " + str(self.preco))
        print("Estoque......... " + str(self.estoque))

