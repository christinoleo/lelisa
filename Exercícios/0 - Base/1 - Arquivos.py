# coding=utf-8
#Desafio: no jogo da forca, ler de um arquivo pra depois continuar o jogo
#Dica: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# crie um arquivo nessa mesma pasta com o texto :)

import random
import sys

def escolherPalavra(text):
    lista1 = []     #lista das palavras do texto
    palavra = ''
    for i in range(len(text)):
        if text[i] != " " and text[i] != "," and text[i] != ".":
            if palavra =='':
                palavra = text[i]
            else:
                palavra = palavra + text[i]
        else:
            if palavra == '':
                lista1 = lista1
            else:
                lista1 = lista1 + [palavra]
                palavra = ''
    y = random.Random().randint(0,len(lista1))
    while len(lista1[y]) <= 5:
        y = random.Random().randint(0, len(lista1))
    return lista1[y]

text = open('texto', 'r').read()
charada = escolherPalavra(text)
print "Bem vindo ao jogo da forca! Sua palavra tem " + str(len(charada)) + " letras."
oculto = ''
for i in range(len(charada)):
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
        for i in range(len(charada)):
            if letras[k] == charada[i]:
                temporario = temporario + charada[i]
            if letras[k] != charada[i]:
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
                print 'Sua palavra era ' + charada + '.'
                sys.exit()
            j = j + 1
        oculto = temporario
        if oculto == charada:
            print 'Parabens, vc ganhou o jogo!'
            sys.exit()
        print oculto
        print 'Letras chutadas:' + str(letras)
        print "Chute outra letra"
        k = k + 1
        letras = letras + ['']