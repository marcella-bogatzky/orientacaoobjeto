from modelos.restaurante import Restaurante #Do arquivo restaurante.app, importar a classe Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_gepreto = Restaurante('massas do Gepreto', 'Italiana')
restaurante_gepreto.receber_avaliacao('Mah', 10)
restaurante_gepreto.receber_avaliacao('Tuta', 8)
restaurante_gepreto.receber_avaliacao('Marcella', 6)

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_brigadeiro = Sobremesa('Brigadeiro', 1.50, 'chocolate', 'pequeno')
restaurante_gepreto.adicionar_no_cardapio(bebida_suco)
restaurante_gepreto.adicionar_no_cardapio(prato_paozinho)
restaurante_gepreto.adicionar_no_cardapio(sobremesa_brigadeiro)

#restaurante_matuta.alternar_status()

def main():
    #Restaurante.listar_restaurantes()
    restaurante_gepreto.exibir_cardapio

if __name__ == '__main__' : 
    main()