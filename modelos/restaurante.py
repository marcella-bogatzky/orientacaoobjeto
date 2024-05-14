class Restaurante:

    restaurantes = [] #Abre uma lista

    def __init__ (self, nome, categoria): #A função __init__ traz um "método construtor" > instância de um objeto que espera alguma informação. "self" serve para garantirmos que cada restaurante terá suas próprias informações
        self.nome = nome
        self.categoria = categoria
        self.ativo = False 
        Restaurante.restaurantes.append(self) #Adiciona na lista

    def __str__(self): # O método __str__ transforma a representação e texto de um objeto para o que for definido. (Auxilia a não exibir o endereço de na memória ao pesquisar o objeto no console)
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()

# print(vars(restaurante_praca)) || vars > define as variáveis e atributos do objeto
# print(dirs(restaurante_praca)) || dirs > mostra tudo com o que o objeto já "nasce" quando é definido a class
