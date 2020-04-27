class point:

    def __init__( self, cards, data ):
        self.incards = 0
        self.cards = cards
        self.data = data
        self.stock = []

    def cal( self ):

        for i in range(3):
            for d in self.data[i]:
                for p in self.cards['figur_p']:
                    if d.find(p) == 0:
                        if d.find('king hearts') == 0 and d.find('ober hearts'):
                            self.incards += 100
                        elif d.find('king diamonds') == 0 and d.find('ober diamonds'):
                            self.incards += 80
                        elif d.find('king clubs') == 0 and d.find('ober clubs'):
                            self.incards += 60
                        elif d.find('king pikes') == 0 and d.find('ober pikes'):
                            self.incards += 40
                        self.incards += self.cards['figur_p'][p]
            self.stock.append( self.incards )
        return self.stock
