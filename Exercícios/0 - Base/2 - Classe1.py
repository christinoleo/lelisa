# coding=utf-8
# Desafio: Praticar o uso de classes. Daqui em diante tudo será a base de classes para que vc exercite
# Refaça (copie e cola) o jogo da forca no modelo de classe:

import random
import sys

class JogoDaForca:

    def mensagemDeInicioDeJogo(self):

        lista1 = []  # lista das palavras do texto
        palavra = ''
        text = open('texto', 'r').read()
        for i in range(len(text)):
            if text[i] != " " and text[i] != "," and text[i] != ".":
                if palavra == '':
                    palavra = text[i]
                else:
                    palavra = palavra + text[i]
            else:
                if palavra == '':
                    lista1 = lista1
                else:
                    lista1 = lista1 + [palavra]
                    palavra = ''
        y = random.Random().randint(0, len(lista1))
        while len(lista1[y]) <= 5:
            y = random.Random().randint(0, len(lista1))
        self.charada = lista1[y]
        print "Bem vindo ao jogo da forca! Sua palavra tem " + str(len(self.charada)) + " letras."

    def loopDoJogo(self):
        oculto = ''
        for i in range(len(self.charada)):
            oculto = oculto + "_"
        print oculto
        print "Chute uma letra."
        letras = ['']
        j = 0
        k = 0
        while j < 6:
            letras[k] = raw_input()
            if letras[k] in letras[0:k]:
                print 'Letra ja utilizada. Chute outra.'
                continue
            else:
                temporario = ''
                for i in range(len(self.charada)):
                    if letras[k] == self.charada[i]:
                        temporario = temporario + self.charada[i]
                    if letras[k] != self.charada[i]:
                        temporario = temporario + oculto[i]
                if oculto == temporario:
                    print 'Errou!'
                    if j == 0:
                        print 'Cabeca na forca'
                    if j == 1:
                        print 'Tronco na forca'
                    if j == 2:
                        print 'Braco direito na forca'
                    if j == 3:
                        print 'Braco esquerdo na forca'
                    if j == 4:
                        print 'Perna direita na forca'
                    if j == 5:
                        print 'Perna esquerda na forca. Vc perdeu :('
                        self.resultado = 0
                        sys.exit()
                    j = j + 1
                oculto = temporario
                if oculto == self.charada:
                    self.resultado = 1
                    sys.exit()
                print oculto
                print 'Letras chutadas:' + str(letras)
                print "Chute outra letra"
                k = k + 1
                letras = letras + ['']

    def mensagemDeFimDeJogo(self):
        if self.resultado == 0:
            print 'Sua palavra era ' + self.charada + '.'
        if self.resultado == 1:
            print 'Parabens, vc ganhou o jogo!'

#não mude nada daqui em diante! Faça funcionar dessa forma :)
jogo = JogoDaForca()
jogo.mensagemDeInicioDeJogo()
jogo.loopDoJogo()
jogo.mensagemDeFimDeJogo()