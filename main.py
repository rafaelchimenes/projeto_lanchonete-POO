import os
from Pedido import Pedido
from Cliente import Cliente
from Produto import Produto
from ItemPedido import ItemPedido

def menuCliente():
    while True:
        os.system("cls")
        print("----  Clientes 👤 ----\n"+
            "1 - 📄 Cadastrar\n"+
            "2 - 🔎 Listar\n"+
            "3 - 📝 Alterar\n"+
            "4 - ❌ Excluir\n"+
            "0 - ⬅️ Sair\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break

def menuProduto():
    while True:
        os.system("cls")
        print("----  Produtos 📦 ----\n"+
            "1 - 📄 Cadastrar\n"+
            "2 - 🔎 Listar\n"+
            "3 - 📝 Alterar\n"+
            "4 - ❌ Excluir\n"+
            "0 - ⬅️ Sair\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break

##main
if __name__ == "__main__":
    while True:
        os.system("cls")
        print("---- Sistema Lanchonete 🥪 ----\n"
            "1 - 👤 Clientes\n"+
            "2 - 📦 Produtos\n"+
            "3 - 🛒 Novo Pedido\n"+
            "0 - ⬅️ Sair\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break
        elif opcao=="1":
            menuCliente()
        elif opcao=="2":
            menuProduto()
    print("\n bye!\n ( ﾟдﾟ)✌️   ")
