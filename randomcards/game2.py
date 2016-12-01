import random


# class Carta:
#     num = 1

class Jog:
    cards = []

    def setNome(self, o_que_o_cara_digitou):
        self.nome = o_que_o_cara_digitou

    def pegarCartas(self):
        for i in range(10):
            self.cards = self.cards + [random.Random().randint(1, 10)]

def loop(jogs):
    for i in range(len(jogs[0].cards)):
        for j in range(2):
            print "Chute um numero, " + jogs[j].nome
            num = int(raw_input())

            if (num == jogs[j].cards[i]):
                print 'parabens, ' + jogs[j].nome + '! Voce acertou!'
                return
            else:
                print 'Voce errou..' + jogs[j].nome + ' o numero era ' + str(jogs[j].cards[i])
                print jogs[j].nome + ', Tente!'

jogs = []
for j in range(2):
    print 'jogador ' + str(j) + ', digite o seu nome'
    jogador = Jog()
    jogador.setNome(raw_input())
    jogador.pegarCartas()
    jogs = jogs + [jogador]

loop(jogs)
print 'Acabou o jogo!'