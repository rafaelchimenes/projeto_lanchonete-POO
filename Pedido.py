class Pedido:
    #não define os atributos
    status="Recebido"
    
    #método construtor - instanciar recebe os valor do objeto
    def __init__(self, num, data, hora, cliente, itens, pag):
       #selft é chamar os atributos;
       self.__num=num#private - não ser acessado nem alterado por outras classes
       self.data=data#publico - pode acessado e alterado por outras classes
       self.hora=hora
       self.cliente=cliente
       self.__itens=itens
       self.pagamento=pag

    #método - ação 
    def atualizar_pedido(self, novoStatus):
        self.status=novoStatus

    def imprimirPedido(self):
        print(f"\n------------- Pedido nº {self.__num} --------------"
              f"\nData: {self.data} -  Horário: {self.hora} "
              f"\nCliente: {self.cliente.nome}"
              f"\nEndereço: {self.cliente.endereco}"
              f"\nTelefone: {self.cliente.getTelefone()}"
              f"\nStatus: {self.status} -  Pagamento: {self.pagamento}"
              f"\n----------------------------------------------")
        for item in self.__itens:
            print(f"Produto: {item.produto.descricao} "
                  f"- Qtd: {item.quantidade} - Valor: {item.produto.preco}" 
                  f"- Total: {item.totalItem()}")
        

    #encapsulamento - METODOS QUE INTERMEDIAM O ACESSO OU A ALTEÇÃO 
    def setNum(self, numero): #setando-alterando indireamente pois num é private
        self.__num=numero

    def getNum(self): #acesar a finformação de variavel private
        return self.__num

    def setIten(self, item): #controla as informações
        self.__itens.append(item)
