import os
from Pedido import Pedido
from Cliente import Cliente
from Produto import Produto

os.system("cls")


#cadastro do cliente
novoCliente = Cliente(endereco="Rua Vital Brasil", email="joao@gmail.com",
                      cpf="033888665598", nome="João Desenvolvedor", tel="679988-6677")
novoCliente.imprimeFicha()

#novo pedido
novoPedido = Pedido(1, "14/09/2026", "21:10", novoCliente,
                    ["X-Salada", "X-bacon"], "Pix")
novoPedido.imprimirPedido()


#cria produto
xbacon =  Produto(cod="P01", desc="X-Bacon", categoria="Lanche", preco=19.90)
xbacon.imprimeProduto()
#criar um ItemPedido
