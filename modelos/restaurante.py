from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = [] #Abre uma lista

    def __init__ (self, nome, categoria): #O método especial __init__ traz um "método construtor" > instância de um objeto que espera alguma informação. "self" serve para garantirmos que cada restaurante terá suas próprias informações
        self._nome = nome.title() #Mantém a primeira letra em maiúscula
        self._categoria = categoria.upper() #Deixa toda a palavra em caixa alta
        self._ativo = False #O _ antes do ativo indica que se trata de um "atributo privado" e que não deve ser mexido. (O _ não impede de fato que seja feita uma alteração, mas indica)
        self._avaliacao = []
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
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1) #Round define a quantidade de casas decimais
        return media

