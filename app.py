from modelos.restaurante import Restaurante #Do arquivo restaurante.app, importar a classe Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_gepreto = Restaurante('massas do Gepreto', 'Italiana')
restaurante_gepreto.receber_avaliacao('Mah', 10)
restaurante_gepreto.receber_avaliacao('Tuta', 8)
restaurante_gepreto.receber_avaliacao('Marcella', 6)

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')

#restaurante_matuta.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__' : 
    main()