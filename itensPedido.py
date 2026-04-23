
class ItensPedido:
    def __init__(self, id_produto,preco,qtd):
        self.id_produto = id_produto
        self.preco = preco
        self.qtd = qtd
        self.subtotal = preco * qtd

    
        
        
