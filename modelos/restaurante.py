class Restaurante:

    restaurantes = [] #Abre uma lista

    def __init__ (self, nome, categoria): #O método especial __init__ traz um "método construtor" > instância de um objeto que espera alguma informação. "self" serve para garantirmos que cada restaurante terá suas próprias informações
        self._nome = nome.title() #Mantém a primeira letra em maiúscula
        self._categoria = categoria.upper() #Deixa toda a palavra em caixa alta
        self._ativo = False #O _ antes do ativo indica que se trata de um "atributo privado" e que não deve ser mexido. (O _ não impede de fato que seja feita uma alteração, mas indica)
        Restaurante.restaurantes.append(self) #Adiciona na lista

    def __str__(self): # O método especial __str__ transforma a representação e texto de um objeto para o que for definido. (Auxilia a não exibir o endereço de na memória ao pesquisar o objeto no console)
        return f'{self._nome} | {self._categoria}'
    
    @classmethod #Método exclusivo para a classe
    def listar_restaurantes(cls): #cls é usado por convenção quando se usa método da classe
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes: 
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property #Método que modifica como um atributo é lido
    def ativo(self):
        return '☒' if self._ativo else '☐' 
    
    def alternar_status(self): #método para os objetos
        self._ativo = not self._ativo

restaurante_gepreto = Restaurante('massas do Gepreto', 'Italiana')
restaurante_gepreto.alternar_status()
restaurante_oberyn = Restaurante('foodtruck do Oberyn', 'Hamburgueria')

Restaurante.listar_restaurantes()

# print(vars(restaurante_praca)) || vars > define as variáveis e atributos do objeto
# print(dirs(restaurante_praca)) || dirs > mostra tudo com o que o objeto já "nasce" quando é definido a class
