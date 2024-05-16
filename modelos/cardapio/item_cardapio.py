from abc import ABC, abstractclassmethod 

class ItemCardapio (ABC):
    def __init__(self, nome, preco): #Todo item do cardápio, independente do tipo, precisa de um nome e um preço
        self._nome = nome
        self._preco = preco

    @abstractclassmethod  #Classe abstrata: queremos que o método sirva de modelo para que outras classes sigam ele
    def aplicar_desconto(self):
        pass


   