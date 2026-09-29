class Produto:

    def __init__(self, cod, desc, categoria, preco):
        self.codigo=cod
        self.descricao=desc
        self.categoria=categoria
        self.preco=preco

    def imprimeProduto(self):
         print(
            f"\n------------- Produto cód. {self.codigo} --------------"
            f"\nDescrição: {self.descricao}"
            f"\nCategoria: {self.categoria}"
            f"\nValor: R$ {self.preco:.2f}"
            f"\n----------------------------------------------"
        )
    
