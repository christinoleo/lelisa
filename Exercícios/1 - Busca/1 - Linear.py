# coding=utf-8
# No estudo das buscas, você deve fazer um algoritimo que encontre um determinado elemento numa lista

class Busca:
    def buscaLinear(self, lista, elemento):
        for i in range(len(lista)):
            if elemento == lista[i]:
                return i + 1
    #
    # def buscaBinaria(self, lista, elemento):
    #     m = int(len(lista)/2.0)
    #     x = int(len(lista)/2.0)
    #     for i in range(int(len(lista))):
    #         if elemento == lista[m]:
    #             return m+1
    #         else:
    #             if lista[m] < elemento:
    #                 m = m + int(x/2)
    #             elif lista[m] > elemento:
    #                 m = m - int(x/2)
    #             if x > 3:
    #                 x = int(x/2)

    def buscaBinaria(self, lista, elemento):
        m = int(len(lista) / 2.0)
        x = int(len(lista) / 2.0)
        fix = int(len(lista) / 2.0)
        for i in range(fix):
            if elemento == lista[m]:
                return x + 1
            else:
                if lista[m] < elemento:
                    lista = lista[m+1:len(lista)]
                    m = int(m/2.0)
                    x = x + m + 1
                if lista[m] > elemento:
                    lista = lista[0:m]
                    m = int(m/2.0)
                    x = x - m - 1



lista = [1,2,3,4,5,6]
busca = Busca()
print(busca.buscaBinaria(lista, 0))