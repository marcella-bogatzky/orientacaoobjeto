from typing import Any, SupportsIndex
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = [] #Abre uma lista

    def __init__ (self, nome, categoria): #O método especial __init__ traz um "método construtor" > instância de um objeto que espera alguma informação. "self" serve para garantirmos que cada restaurante terá suas próprias informações
        self._nome = nome.title() #Mantém a primeira letra em maiúscula
        self._categoria = categoria.upper() #Deixa toda a palavra em caixa alta
        self._ativo = False #O _ antes do ativo indica que se trata de um "atributo privado" e que não deve ser mexido. (O _ não impede de fato que seja feita uma alteração, mas indica)
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) #Adiciona na lista

    def __str__(self): # O método especial __str__ transforma a representação e texto de um objeto para o que for definido. (Auxilia a não exibir o endereço de na memória ao pesquisar o objeto no console)
        return f'{self._nome} | {self._categoria}'
    
    @classmethod #Método exclusivo para a classe
    def listar_restaurantes(cls): #cls é usado por convenção quando se usa método da classe
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes: 
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') #"str" em "{str(restaurante.media_avaliacoes).ljust(25)}" serve para transformar o resultado número em texto

    @property #Método que modifica como um atributo é lido
    def ativo(self):
        return '☒' if self._ativo else '☐' 
    
    def alternar_status(self): #método para os objetos
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        if nota > 5: #Acrescentei à solução apresentada pela plataforma, para caso restaurante receba um valor acima de 5, seja computado como 5
            avaliacao = Avaliacao(cliente, 5)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1) #Round define a quantidade de casas decimais
        return media

    # def adicionar_bebida_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida)

    # def adicionar_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print (f'Cardapio do restaurante {self._nome} \n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):  #hasattr é "has attributte" > se tiver o atributo
                mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            if hasattr(item, 'tipo') and hasattr(item, 'tamanhos'):  #hasattr é "has attributte" > se tiver o atributo
                mensagem_sobremesa = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tipo: {item.tipo} | Tamanho: {item.tamanhos}'
                print(mensagem_sobremesa)
            if hasattr(item, 'tamanho'):
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)