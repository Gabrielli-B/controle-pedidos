from itensPedido import ItensPedido
import manipulacaoMenu


def menu():
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Atualizar  Produto")
    print("4 - Remover  Produto")
    print("5 - Novo Pedido")
    print("6 - Ver Pedidos")
    print("7 - Sair")

op=0

while(op != 7):
    menu()
    op=int(input("Escolha uma opção: "))

    if(op == 1):
       manipulacaoMenu.menuInserir()
    elif(op==2):
        manipulacaoMenu.menuListar()
    elif(op==3):
        manipulacaoMenu.menuAtualizar()
    elif(op==4):
        manipulacaoMenu.menuRemover()
    elif(op==5):
        manipulacaoMenu.menuNovoPedido()
    elif(op==6):
        manipulacaoMenu.menuVerPedidos()

