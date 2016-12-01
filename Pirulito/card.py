NAIPES = ['E','C','P','O']

class card:
    def __init__(self, number, naipe):
        self.number = number
        self.naipe = naipe

    def print_card(self):
        print self.number + self.naipe