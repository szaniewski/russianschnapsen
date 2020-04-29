class play:
    def __init__( self, cards, opponents, playernam, *trumps ):
        self.cards = cards
        self.figurspowers = self.cards.get('figur_p')
        self.winer = ''
        self.opponents = opponents
        self.playernam = playernam
        self.trumpsuit = trumps
        self.playerone = self.playernam[0]
        self.playeronecolor = self.opponents[0].split(' ')[1]
        self.playeronefigur = self.opponents[0].split(' ')[0]
        self.playertwo = self.playernam[1]
        self.playertwocolor = self.opponents[1].split(' ')[1]
        self.playertwofigur = self.opponents[1].split(' ')[0]

    def cal( self ):

        if self.playeronecolor != self.playertwocolor:
            self.winer = self.playerone
        else:
            if self.figurspowers.get( self.playeronefigur ) > self.figurspowers.get( self.playertwofigur ):
                self.winer = self.playerone
            else:
                self.winer = self.playertwo

        return self.winer

    def result( self ):

        if self.trumpsuit:
            if self.playeronecolor ==  self.trumpsuit:
                self.winer = self.playerone
            elif self.playertwocolor ==  self.trumpsuit:
                self.cal()
        else:
            self.cal()

        return self.winer
