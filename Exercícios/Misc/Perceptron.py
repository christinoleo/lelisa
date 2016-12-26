# coding=utf-8
# http://computing.dcu.ie/~humphrys/Notes/Neural/single.neural.html
# Usando o que está escrito acima, crie uma classe Perceptron
# O construtor (__init__) receberá quantas entradas ele tem
# A classe terá 2 funções: calcula e aprende
# calcula recebe uma lista de entradas e calcula a saida
# aprende recebe uma lista de entradas e a saída esperada,
#   e muda os pesos (w) caso tenha errado conforme a seção Perceptron Learning Rule do site

import random

class Perceptron:
    def __init__(self, tamanho_da_entrada):
        self.tamanho = tamanho_da_entrada
        pesos = []
        for i in range(self.tamanho):
            if i == 0:
                pesos = [random.Random().random()]
            else:
                pesos = pesos + [random.Random().random()]
        self.w = pesos

    def calcula(self, entradas):
        soma = 0
        for i in range(self.tamanho):
            soma = soma + entradas[i] + self.w[i]
        if soma >= 0.5:
            self.saida = 1
        else:
            self.saida = 0
        return self.saida

    def aprende(self, entradas, saida_esperada):
        soma = 0
        c = 0.05
        self.saida = self.calcula(entradas)
        # while True:
        if self.saida == saida_esperada:
            return self.saida
        else:
            if self.saida < saida_esperada:
                novos_pesos = []
                for i in range(self.tamanho):
                    if i == 0:
                        novos_pesos = [self.w[i] + c]
                    else:
                        novos_pesos = novos_pesos + [self.w[i] + c]
                self.w = novos_pesos
            if self.saida > saida_esperada:
                novos_pesos = []
                for i in range(self.tamanho):
                    if i == 0:
                        novos_pesos = [self.w[i] - c]
                    else:
                        novos_pesos = novos_pesos + [self.w[i] - c]
                self.w = novos_pesos

# nao mexe a partir daqui.. vou fazer uma porta AND
neuronio_cadeira = Perceptron(2)
neuronio_mesa = Perceptron(2)
neuronio_cama = Perceptron(2)

for i in range(20):
    neuronio_cadeira.aprende([0.5,0.5], 1)
    neuronio_cadeira.aprende([0.5,0.1], 0)
    neuronio_cadeira.aprende([0.5,1], 0)

    neuronio_mesa.aprende([0.5,0.5], 0)
    neuronio_mesa.aprende([0.5,0.1], 1)
    neuronio_mesa.aprende([0.5,1], 0)

    neuronio_cama.aprende([0.5,1], 0)
    neuronio_cama.aprende([0.5,0.5], 0)
    neuronio_cama.aprende([0.5,1], 1)

print(neuronio_cadeira.calcula([1,1]))
print(neuronio_mesa.calcula([1,0.5]))
print(neuronio_cama.calcula([1,3]))
