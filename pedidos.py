class Pedidos:
    def __init__(self, data, valorTotal=0, idPedido=None):
        self.data = data
        self.valorTotal = valorTotal
        self.idPedido = idPedido
        self.itens=[]

    def adicionarItem(self,item):
        self.itens.append(item)
        self.valorTotal+=item.subtotal

