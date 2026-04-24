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
