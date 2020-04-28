class point:

    def __init__( self, cards, data ):
        self.incards = 0
        self.cards = cards
        self.data = data
        self.stocks = []

    def cal( self ):

        for i in range(3):
            for d in self.data[i]:
                for p in self.cards['figur_p']:
                    if d.find(p) == 0:
                        self.incards += self.cards['figur_p'][p]
                    if p.find('king hearts') == 0 and p.find('ober hearts'):
                        self.incards += 100
                    elif p.find('king diamonds') == 0 and p.find('ober diamonds'):
                        self.incards += 80
                    elif p.find('king clubs') == 0 and p.find('ober clubs'):
                        self.incards += 60
                    elif p.find('king pikes') == 0 and p.find('ober pikes'):
                        self.incards += 40
            self.stocks.append( [self.incards] )

        return self.stocks
