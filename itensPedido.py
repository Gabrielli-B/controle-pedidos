
class ItensPedido:
    def __init__(self, id_produto,id_pedido,qtd,subtotal,id_item=None):
        self.id_produto = id_produto
        self.id_pedido = id_pedido
        self.qtd = qtd
        self.subtotal = subtotal
        self.id_item = id_item
        
        
