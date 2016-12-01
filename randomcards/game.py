import random

def loop(cards, jogs):
    for i in range(len(cards[0])):
        for j in range(2):
            print "Chute um numero, " + jogs[j]
            num = int(raw_input())
            print "Agora chute o nipe, " + jogs[j]
            naipe = int(raw_input())

            if ([num, naipe] == cards[j][i]):
                print 'parabens, ' + jogs[j] + '! Voce acertou!'
                return
            else:
                print 'Voce errou..' + jogs[j] + ' o numero era ' + str(cards[j][i])

jogs = []
cards = []
for j in range(2):
    print 'jogador ' + str(j) + ', digite o seu nome'
    jogs = jogs + [raw_input()]
    cards_de_dentro = []
    for i in range(10):
        cards_de_dentro = cards_de_dentro + [[random.Random().randint(1,2), random.Random().randint(1,1)]]
    cards = cards + [cards_de_dentro]

loop(cards, jogs)
print 'Acabou o jogo!'