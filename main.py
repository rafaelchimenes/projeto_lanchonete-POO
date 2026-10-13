import os
from Pedido import Pedido
from Cliente import Cliente
from Produto import Produto
from ItemPedido import ItemPedido

listaClientes = []
listaProdutos = []

def buscarCliente(cpf) -> int:
    i=0
    for cliente in listaClientes:
        if cliente.cpf==cpf:
            return i
        i=i+1
    return None

def buscarProduto(cod) ->int:
    posicao=None
    for i, prod in enumerate(listaProdutos):
        if prod.codigo==cod:
            posicao=i
            break
    return posicao


def menuCliente():
    while True:
        os.system("cls")
        print("----  Clientes 👤 ----\n"+
            "1 - 📄 Cadastrar Cliente\n"+
            "2 - 🔎 Listar Cliente\n"+
            "3 - 📝 Alterar Cliente\n"+
            "4 - ❌ Excluir Cliente\n"+
            "0 - ⬅️ Voltar\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break
        elif opcao=="1":
            os.system("cls")
            print("---- 📄 Cadastrar Cliente  ----\n")
            nome=input("Nome do Cliente:")
            cpf=input("CPF:")
            telefone=input("Telefone:")
            endereco=input("Endereço:")
            mail=input("E-mail:")

            novo = Cliente(nome=nome,cpf=cpf,email=mail,endereco=endereco, tel=telefone)
            listaClientes.append(novo)
            input("\n\nSalvo com sucesso!\nDigite algo para voltar.")

        elif opcao=="2":
            for cliente in listaClientes:
                cliente.imprimeFicha()
            input("\n\nDigite algo para voltar.")

        elif opcao =="3":
            os.system("cls")
            print("---- 📝 Alterar Cliente  ----\n")
            cpf = input("Informe o CPF do Cliente:")
            posicao=buscarCliente(cpf)
            if posicao is None:    
                input(f"\n!Não {cpf} encontrado.... \n\nDigite algo para voltar.")
            else:
                cliente=listaClientes[posicao]
                cliente.nome=input(f"Nome: {cliente.nome} alterar para:")
                cliente.setTelefone(input("Telefone:"))
                cliente.email=input("E-mail:")
                cliente.endereco=input("Endereço:")
                listaClientes[posicao]=cliente
                input(f"\n!Cliente alterado com sucesso.... \n\nDigite algo para voltar.")


        elif opcao =="4":
            os.system("cls")
            print("---- ❌ Excluír Cliente  ----\n")
            cpf = input("Informe o CPF para a Exclusão:\n")
            posicao = buscarCliente(cpf)
            if posicao!=None:
                listaClientes.pop(posicao)
                input("\nExcluído com sucesso!.... \n\nDigite algo para voltar.")
            else:
                input(f"\n!Não {cpf} encontrado.... \n\nDigite algo para voltar.")

def menuProduto():
    while True:
        os.system("cls")
        print("----  Produtos 📦 ----\n"+
            "1 - 📄 Cadastrar Produto\n"+
            "2 - 🔎 Listar Produto\n"+
            "3 - 📝 Alterar Produto\n"+
            "4 - ❌ Excluir Produto\n"+
            "0 - ⬅️ Voltar\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break
        if opcao=="1":
            os.system("cls")
            print("---- 📦 Cadastrar de Produtos  ----\n")
            cod=input("Código:")
            desc=input("Descrição:")
            cat=input("Categoria:")
            preco=float(input("Preço:"))
            novo = Produto(cod=cod, categoria=cat, desc=desc, preco=preco)
            listaProdutos.append(novo)
            input("\n\nSalvo com sucesso!\nDigite algo para voltar.")

        if opcao=="2":
            for produto in listaProdutos:
                produto.imprimeProduto()
            input("\n\nDigite algo para voltar.")
        elif opcao =="3":
            os.system("cls")
            print("---- 📝 Alterar Produto  ----\n")
            cod = input("Informe o CPF do Cliente:")
            posicao=buscarProduto(cod)
            if posicao is None:    
                input(f"\nProduto {cod} não encontrado!.... \n\nDigite algo para voltar.")
            else:
                prod=listaProdutos[posicao]
                prod.descricao=input(f"Descrição: {prod.descricao} trocar para:")
                prod.categoria=input(f"categoria: {prod.categoria} trocar para:")
                prod.preco=float(input(f"preco: {prod.preco} trocar para:"))            
                listaProdutos[listaProdutos]=prod
                input(f"\n!Produto alterado com sucesso.... \n\nDigite algo para voltar.")
        elif opcao =="4":
            os.system("cls")
            print("---- ❌ Excluír Produto  ----\n")
            cod = input("Informe o Código do produto para a Exclusão:\n")
            posicao = buscarProduto(cod)
            if posicao!=None:
                listaProdutos.pop(posicao)
                input("\nExcluído com sucesso!.... \n\nDigite algo para voltar.")
            else:
                input(f"\n {cod} não encontrado!.... \n\nDigite algo para voltar.")
        
            
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
