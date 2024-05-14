from modelos.restaurante import Restaurante #Do arquivo restaurante.app, importar a classe Restaurante

restaurante_gepreto = Restaurante('massas do Gepreto', 'Italiana')
restaurante_gepreto.receber_avaliacao('Mah', 10)
restaurante_gepreto.receber_avaliacao('Tuta', 8)
restaurante_gepreto.receber_avaliacao('Marcella', 6)
restaurante_matuta = Restaurante('rancho da Matuta', 'Caipira')
#restaurante_mirna = Restaurante('peixotescos da Mirna', 'Japonesa')

#restaurante_matuta.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__' : 
    main()