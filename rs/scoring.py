class point:

    def __init__( self, cards, data ):
        self.incards = 0
        self.cards = cards
        self.data = data
        self.stock = []

    def cal( self ):
        for d in self.data[0]:
            for p in self.cards['figur_p']:
                if d.find(p) == 0:
                    self.incards += self.cards['figur_p'][p]
        self.stock.append( self.incards )

        return self.stock
