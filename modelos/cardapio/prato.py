from modelos.cardapio.item_cardapio import ItemCardapio 
#Queremos que essa classe "herde" características da classe pai ItemCardapio disponível em "item_cardapio.py"

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super ().__init__(nome,preco) #"Super" permite que a gente acesse informações de outra classe. Esse conceito é chamado de "Herança"
        #Porém, exstem também informações próprias da classe prato, e precisamos indicá-las normalmente:
        self.descricao = descricao

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)