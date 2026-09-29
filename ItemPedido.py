class ItemPedido:

    def __init__(self, produto, obs, qtd, desconto):
        self.produto=produto
        self.obsercacao=obs
        self.quantidade=qtd
        self.desconto=desconto


    def totalItem(self):
        return (self.quantidade*self.produto.preco)-self.desconto
        
