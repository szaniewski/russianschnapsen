class play:
    def __init__( self, cards, opponents, playernam ):
        self.cards = cards
        self.winer = ''
        self.opponents = opponents
        self.playernam = playernam

    def cal( self ):

        figurs_powers = self.cards.get('figur_p')

        if self.opponents[0].split(' ')[1] != self.opponents[1].split(' ')[1]:
            self.winer = self.playernam[0]
        else:
            if figurs_powers.get(self.opponents[0].split(' ')[0]) > figurs_powers.get(self.opponents[1].split(' ')[0]):
                self.winer = self.playernam[0]
            else:
                self.winer = self.playernam[1]
        return self.winer
