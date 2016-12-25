# coding=utf-8
# http://computing.dcu.ie/~humphrys/Notes/Neural/single.neural.html
# Usando o que está escrito acima, crie uma classe Perceptron
# O construtor (__init__) receberá quantas entradas ele tem
# A classe terá 2 funções: calcula e aprende
# calcula recebe uma lista de entradas e calcula a saida
# aprende recebe uma lista de entradas e a saída esperada,
#   e muda os pesos (w) caso tenha errado conforme a seção Perceptron Learning Rule do site

class Perceptron:
    def __init__(self, tamanho_da_entrada):
        pass

    def calcula(self, entradas):
        pass

    def aprende(self, entradas, saida_esperada):
        pass

# nao mexe a partir daqui.. vou fazer uma porta AND
neuronio = Perceptron(2)

for i in range(20):
    neuronio.aprende([0,0], 0)
    neuronio.aprende([0,1], 0)
    neuronio.aprende([1,0], 0)
    neuronio.aprende([1,1], 1)

print(neuronio.calcula([0,0]))
print(neuronio.calcula([0,1]))
print(neuronio.calcula([1,0]))
print(neuronio.calcula([1,1]))