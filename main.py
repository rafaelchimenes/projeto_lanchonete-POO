import os
from Pedido import Pedido
from Cliente import Cliente
from Produto import Produto
from ItemPedido import ItemPedido

os.system("cls")
#Cadastrar Cliente
novoCli = Cliente(nome="João Desenvolvedor", cpf="03344455512", 
            email="joao@dev.com", endereco="Rua Tal, nº00",tel="6799999999")

#Cadastrar Produto
siri = Produto(cod=1, desc="Hambúrguer de Siri", categoria="Lanche",
             preco=20.55)
refri = Produto(cod=2, desc="Tubaíana", categoria="Bebidas",
             preco=5.6)

#pedido
item1 =  ItemPedido(produto=siri,obs="Cebola Extra",  qtd=2, desconto=2)
item2 = ItemPedido(produto=refri, obs="",  qtd=2, desconto=0)

itens = [item1,item2]

pedido = Pedido(cliente=novoCli, data="28/09/2026", hora="21:30",
                itens=itens, pag="pix",num=1) 