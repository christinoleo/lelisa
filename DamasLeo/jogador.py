import peca

class jogador:
    def __init__(self, funcao):
        if funcao == 'auto':
            self.auto = True
        else:
            self.auto = False

        # tem 8 pecas

        self.pecas = []

        if not self.auto:
            for i in range(12):
                print self.posicao_peca(i)
                self.pecas = self.pecas + \
                             [peca.peca(self.posicao_peca(i))]
        else:
            for i in range(20,32):
                print self.posicao_peca(i)
                self.pecas = self.pecas + \
                             [peca.peca(self.posicao_peca(i))]

    def posicao_peca(self, id):
        resto = (id/4.0 - int(id/4.0))*4
        if int(int(id/4.0)/2.0) == int(id/4.0)/2.0:
            return [int(id/4.0), resto*2]
        else:
            return [int(id/4.0), resto*2+1]

