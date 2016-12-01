class gui:
    old_cards = []

    def clear(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def print_games(self, games):
        for game in games:
            if game[0][0] == game[1][0]:
                print 'Lavadeira: ' + str(game)
            else:
                print 'Sequencia: ' + str(game)

    def print_last_card(self, card):
        print 'Descartes: ' + str(card)
        if len(self.old_cards) > 1: print 'Anteriores: ' + str(self.old_cards[-1]) + ' ' + str(self.old_cards[-2])
        self.old_cards = self.old_cards + [card]