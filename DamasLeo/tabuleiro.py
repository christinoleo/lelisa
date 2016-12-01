class tabuleiro:
    def __init__(self, player1, player2):
        self.humano = player1
        self.ia = player2

    def imprime(self):
        # imprimir as pecas
        # self.humano.imprime_pecas()
        print '\n\n\n\n\n\n\n\n\n\n\n'

        for y in range(8):
            linha = ''
            for x in range(8):
                ja_colocou = False
                for peca in self.humano.pecas:
                    if peca.x == x and peca.y == y:
                        linha = linha + 'X|'
                        ja_colocou = True
                        break
                for peca in self.ia.pecas:
                    if peca.x == x and peca.y == y:
                        linha = linha + 'O|'
                        ja_colocou = True
                        break

                # se nao colocou nada ainda
                if not ja_colocou:
                    linha = linha + '_|'
            print linha