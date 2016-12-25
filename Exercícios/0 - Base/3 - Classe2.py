# coding=utf-8
# Muito bem! Vamos usar umas funções padrão de classe
#Desafio: Fazer uma Classe que sirva como numero complexo

class ComplexNumber:

    def setRealNumber(self, number: float):
        self.realNumber = number

    def getRealNumber(self):
        return self.realNumber

    def setComplexNumber(self, number: float):
        self.complexNumber = number

    def getComplexNumber(self):
        return self.complexNumber

    def add(self, anotherComplexNumber): #soma o numero dessa classe com o numero passado por argumento
        self.realNumber = self.realNumber + anotherComplexNumber.realNumber
        self.complexNumber = self.complexNumber + anotherComplexNumber.complexNumber

    def subtract(self, anotherComplexNumber): #subtrai o numero dessa classe com o numero passado por argumento
        self.realNumber = self.realNumber - anotherComplexNumber.realNumber
        self.complexNumber = self.complexNumber - anotherComplexNumber.complexNumber

    def multiply(self, anotherComplexNumber): #multiplica o numero dessa classe com o numero passado por argumento
        self.realNumber = self.realNumber * anotherComplexNumber.realNumber
        self.complexNumber = self.complexNumber * anotherComplexNumber.complexNumber

    def divide(self, anotherComplexNumber): #divide o numero dessa classe com o numero passado por argumento
        self.realNumber = self.realNumber / anotherComplexNumber.realNumber
        self.complexNumber = self.complexNumber / anotherComplexNumber.complexNumber

    def isEqual(self, anotherComplexNumber): # retorna true/false se for igual a outro numero
        if self.realNumber == anotherComplexNumber.realNumber:
            return True
        else:
            return False


    #depois de completar essas funções, olhe na pagina a baixo e faça o 'overload' das seguintes funçoes
    # https://www.programiz.com/python-programming/operator-overloading
    # a pagina faz algo parecido com essa classe, mas ao inves de ser num complexo é ponto cartesiano 2D (x,y)

    def __add__(self, other):
        result = ComplexNumber()
        result.setRealNumber(self.realNumber + other.realNumber)
        result.setComplexNumber(self.complexNumber + other.complexNumber)
        return result

    def __sub__(self, other):
        result = ComplexNumber()
        result.setRealNumber(self.realNumber - other.realNumber)
        result.setComplexNumber(self.complexNumber - other.complexNumber)
        return result

    def __mul__(self, other):
        result = ComplexNumber()
        result.setRealNumber(self.realNumber * other.realNumber)
        result.setComplexNumber(self.complexNumber * other.complexNumber)
        return result

    def __div__(self, other):
        result = ComplexNumber()
        result.setRealNumber(self.realNumber / other.realNumber)
        result.setComplexNumber(self.complexNumber / other.complexNumber)
        return result

    def __str__(self):
        return str(self.getRealNumber()) + '+' + str(self.getComplexNumber()) + 'i'

# não mude nada daqui em diante! Faça funcionar dessa forma :)

complex_number_1 = ComplexNumber()
complex_number_2 = ComplexNumber()

complex_number_1.setRealNumber(0)
complex_number_1.setComplexNumber(5)
complex_number_2.setRealNumber(3)
complex_number_2.setComplexNumber(4)

print(str(complex_number_1.getRealNumber()) + '+' + str(complex_number_1.getComplexNumber()) + 'i')
print(str(complex_number_2.getRealNumber()) + '+' + str(complex_number_2.getComplexNumber()) + 'i')

#ate aqui, ja funciona.. entenda o porque

complex_number_3 = ComplexNumber()
complex_number_3.setRealNumber(0)
complex_number_3.setComplexNumber(0)

# complex_number_3.add(complex_number_2)
# print str(complex_number_3.getRealNumber()) + '+' + str(complex_number_3.getComplexNumber()) + 'i'
#
# complex_number_3.subtract(complex_number_1)
# print str(complex_number_3.getRealNumber()) + '+' + str(complex_number_3.getComplexNumber()) + 'i'
#
# complex_number_3.multiply(complex_number_1)
# print str(complex_number_3.getRealNumber()) + '+' + str(complex_number_3.getComplexNumber()) + 'i'
#
# complex_number_3.divide(complex_number_2)
# print str(complex_number_3.getRealNumber()) + '+' + str(complex_number_3.getComplexNumber()) + 'i'

#ate aqui precisa das primeiras funçoes so

print(complex_number_1 + complex_number_2)
# print str(complex_number_1 - complex_number_2)
# print str(complex_number_1 * complex_number_2)
# print str(complex_number_1 / complex_number_2)
#
# complex_number_result = complex_number_1 + complex_number_2
# print str(complex_number_result)
#
# complex_number_4 = ComplexNumber()
# complex_number_4.setRealNumber(0)
# complex_number_4.setComplexNumber(0)
#
# complex_number_4.add(complex_number_2)
# complex_number_4.subtract(complex_number_1)
# complex_number_4.multiply(complex_number_1)
# complex_number_4.divide(complex_number_2)
# print str(complex_number_4)

#agora precisa de todas