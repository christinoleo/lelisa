# import vrep # importa o outro arquivos com funcoes
# vrep.connect() # conecta esse programa com o simulador
# vrep.setRightSpeed(0.1) # seta velocidade da roda da direita
# vrep.disconnect() # seta velocidade da roda da esquerda

import random

a = 10
soma = 0

for i in range (a+1):
    if i <= 10:
        x = i
    else:
        x = i*2
    y = x/2.0
    if int(y) == y:
        soma = soma + x
    else:
        soma = soma
# resposta = random.Random().randint(0,soma)
# chute = random.Random().randint(soma+1,soma+5)
# while chute != resposta:
#     print "Chute um valor de zero a "+str(soma)
#     chute = input ()
#     if chute == resposta:
#         print "Parabens,voce acertou"
#     else:
#         print "Errou!"
#         if chute > resposta:
#             print "Foi muito alto."
#         else:
#             print "Foi muito baixo."

def acresc (lista, x):
    lista2 = lista + [random.Random().randint(0,x)]
    for i in range(len(lista), 0, -1):
        if lista2[i] > lista2[i-1]:
            x = lista2[i]
            y = lista2[i-1]
            lista2[i-1] = x
            lista2[i] = y
    return lista2



lista = []
for i in range(0, soma):
    lista = acresc(lista, soma)
print lista











