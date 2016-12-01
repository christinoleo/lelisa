import jogador
import tabuleiro

print 'Bem vindo!'

# dividir os jogadores
humano = jogador.jogador('manual')
ia = jogador.jogador('auto')

# criar o tabuleiro e imprimir
tabuleiro = tabuleiro.tabuleiro(humano, ia)

while True:
    tabuleiro.imprime()

    # pedir o movimento do jogador 1
    humano.pedir_movimento()

    # mexo
    # humano.move()

    # IA mexer do outro lado
    # ia.move()

    # volta ate um jogador num ter mais pecas
    # if tabuleiro.fim():
    break

# fim
print 'FIM'










