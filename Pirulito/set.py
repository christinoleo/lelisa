class set:
    def __init__(self, cards):
        self.cards = cards

    def print_set(self):
        for card in self.cards:
            print card.print_card()