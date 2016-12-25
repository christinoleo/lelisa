# coding=utf-8
# muito bem!! Vamos seguir..
# O que aprender: O encapsulamento de classes!
# Um dos outros principais conceitos de classes é que ela resolva o que ela detem
# Nesse sentido, existe coisas que ela precisa mostrar pros outros (variaveis e funções públicas)
# e outras que não pode mostrar pros outros (variáveis e funções privadas)
# Os que são privados em python comecam com _ ou __
# Você percebeu que no exemplo da aula 3 vc nunca escreveu complex_number.__add__ ou complex_number.__str__?
# São métodos privados! Você não consegue usar assim, mas o python usa esses metodos pra poder descrever o que
# acontece quando se usa um str() ou +

# Um outro método assim é o __init__, que é uma função privada que o python usa quando vc cria
# uma instancia da classe
#Exemplo:

class Pai:
    def __init__(self):
        self.__private_number = '8282828282'
        self.public_number = '52525252525'

janio = Pai() #executa o __init__ aqui
print(janio.public_number) # pega o numero publico e imprime
# print (janio.__private_number) # não funciona! Teste descomentando essa linha

# O __init__ também pode receber coisas:

class Mae:
    def __init__(self, ddd):
        self.__private_number = str(ddd) + '8282828282'
        self.public_number = str(ddd) + '52525252525'

ana = Mae(91) #executa o __init__ aqui
print(ana.public_number) # pega o numero publico e imprime junto com o ddd
# print (ana.__private_number) # não funciona denovo!

# Variáveis e funções privadas são usadas pra evitar que o código fique confuso.
# Dai quem fez uma classe so libera a informação o que os outros tem que ver pra funcionarem

#Desafio: Você ta fazendo uma classe que criptografa e descriptografa um texto!
# Se quem usar seu código puder ver a chave, consegue descobrir o que ta criptografado!
# Proteja sua chave!!
# o codigo de criptografia é: chave é um numero em que você adiciona em todos os caracteres do texto
# pra pegar o numero de uma letra use ord() e pra pegar a letra a partir do numero use chr()
# isso por exemplo adiciona 10 (a chave) na letra c: chr(ord('c')+10)

import random

class Criptographer:
    def __init__(self): #criar uma chave privada randomica
        self.__chave = random.Random().randint(2,40)

    def criptograph(self, text: str) -> str:
        self.textoMudado = ''
        for i in range(len(text)):
            numeroDaLetra = ord(text[i])
            letraMudada = chr(int(numeroDaLetra*self.__chave))
            if i == 0:
                self.textoMudado = letraMudada
            else:
                self.textoMudado = self.textoMudado + letraMudada
        return self.textoMudado # retorna o text cripografado

    def decriptograph(self, criptographed_text: str) -> str:
        self.textoOriginal = ''
        for i in range(len(criptographed_text)):
            numeroDaLetra = ord(criptographed_text[i])
            letraOriginal = chr(int(numeroDaLetra / self.__chave))
            if i == 0:
                self.textoOriginal = letraOriginal
            else:
                self.textoOriginal = self.textoOriginal + letraOriginal
        return self.textoOriginal # retorna o text descripografado

# Não Mexer nada depois daqui!
cript = Criptographer()
texto = 'Legal!'
texto_criptografado = cript.criptograph(texto)
print(texto_criptografado)
texto_de_volta = cript.decriptograph(texto_criptografado)
print(texto_de_volta)

