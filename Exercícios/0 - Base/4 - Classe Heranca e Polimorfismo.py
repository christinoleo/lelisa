# coding=utf-8
# muito bem!! Vamos seguir..
# O que aprender: usar a hierarquia das classes. Tudo o que a classe pai faz, a classe filha também faz
#Exemplo:

class Pai:
    def imprime(self):
        print('Pai')

class Filho(Pai): #assim que fala qual a classe pai
    pass

# descomenta pra ver
pai = Pai()
pai.imprime() #imprime pai
filho = Filho()
filho.imprime() #imprime pai tb

# dai vc pode mudar o que uma funçao do pai faz no filho caso vc queira.. por exemplo:

class Filho2(Pai):
    def imprime(self):
        print('Filho') #agora fai imprimir filho

# descomenta pra ver
pai = Pai()
pai.imprime()  # imprime pai
filho2 = Filho2()
filho2.imprime()  # imprime filho agora

# se vc colocar funções no pai, todos os filhos vao ter a função
# se vc colocar funções no filho, o pai não pode usar!

#Desafio: Faça uma to-do list!
# cada item da lista tem um texto e um título
# mas os itens podem ser meramente um texto, uma marcação na agenda (ter data) ou ter tb uma lista de coisas

class ToDoItem:
    def setText(self, text_sent: str):
        self.text = text_sent

    def setTitle(self, title_sent: str):
        self.title = title_sent

    def getText(self) -> str:
        return self.text

    def getTitle(self) -> str:
        return self.title

    def __str__(self) -> str:
        return 'Title: ' + self.getTitle() + '  text: ' + self.getText()

class ToDoDateItem(ToDoItem): #sobrescreva os dois getCoisa pra retornar texto incluindo a data
    def setDate(self, date_sent: str):
        self.date = date_sent

    def getDate(self) -> str:
        return self.date

    # def getText(self) -> str:
    #     return self.text + ' date: ' + self.getDate()

    def __str__(self) -> str:
        return 'Title: ' + self.getTitle() + '  text: ' + self.getText() + '  date:  ' + self.getDate()

class ToDoListItem(ToDoItem):  # sobrescreva os dois getCoisa pra retornar texto incluindo a lista
    def setList(self, list_sent: list):
        self.list = list_sent

    def getList(self) -> list:
        return self.list

    def __str__(self) -> str:
        return 'Title: ' + self.getTitle() + '  text: ' + self.getText() + '  list:  ' + str(self.getList())

# não mude nada daqui em diante! Faça funcionar dessa forma :)
import random

coisas_a_fazer = []
for i in range(10):
    num_randomico = random.Random().randint(0,3)#o num 3 é pra não acrecentar nada mesmo
    if num_randomico == 0:
        item_a_adicionar_na_lista = ToDoItem()
        item_a_adicionar_na_lista.setText('Texto')
        item_a_adicionar_na_lista.setTitle('Titulo')
        coisas_a_fazer = coisas_a_fazer + [str(item_a_adicionar_na_lista)]
    elif num_randomico == 1:
        item_a_adicionar_na_lista = ToDoDateItem()
        item_a_adicionar_na_lista.setText('Texto de data')
        item_a_adicionar_na_lista.setTitle('Titulo de data')
        item_a_adicionar_na_lista.setDate('4 de Nov')
        coisas_a_fazer = coisas_a_fazer + [str(item_a_adicionar_na_lista)]
    elif num_randomico == 2:
        item_a_adicionar_na_lista = ToDoListItem()
        item_a_adicionar_na_lista.setText('Texto de lista')
        item_a_adicionar_na_lista.setTitle('Titulo de lista')
        item_a_adicionar_na_lista.setList(['1','2','3'])
        coisas_a_fazer = coisas_a_fazer + [str(item_a_adicionar_na_lista)]


for coisa in coisas_a_fazer:
    print(coisa)

