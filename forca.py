import random

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

import sys
text="The master's project, abbreviated hence forth as, fits in the context of research and development of three-dimensional sensor data processing methods applied to mobile robotics. Such methods will be called services in this project, which include a 3D point cloud preprocessing algorithms with data segmentation, separation and identification of planar areas (ground track), and also detecting elements of interest (borders, barriers). Due to the large amount of data to be processed in a short time, these services should use parallel processing, using the GPU to perform partial or complete processing of these data. The application area in focus in this project aims to provide services for an ADAS system: autonomous and intelligent vehicles, forcing them to get close to a real-time processing system due to the autonomous direction of context."
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