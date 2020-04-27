import random
from . import scoring

class cards:

    def __init__( self ):
        self.playerheand = []
        self.gams_card = []
        self.cards = {
            'figur' : 4,
            'figur_p' : {
                'ass': 11,
                'ten': 10,
                'king': 4,
                'ober': 3,
                'unter': 2,
                'nine': 0
            },
            'marriage_p' : {
                'hearts': 100,
                'diamonds': 80,
                'clubs': 60,
                'pikes': 40
            }
        }
        self.gamesruls = {
            'heand': 10,
            'stos': 4
        }

    def deck( self ):
        """
        The deck
        create deck fo game
        """
        for card in self.cards['figur_p']:
            for color in list( self.cards['marriage_p'].keys() ):
                self.gams_card.append( card + ' ' + color )
        return self.gams_card

    def shuffling( self ):
        """
        First hend cards
        """
        random.shuffle( self.gams_card )
        self.playerheand += [self.gams_card[:10]]
        self.playerheand += [self.gams_card[10:20]]
        self.playerheand += [self.gams_card[21:]]

        return self.playerheand

    def playerscoring( self ):
        """
        Cal player point in headn
        """
        self.s = scoring.point( self.cards, self.playerheand )
        point = self.s.cal()
        return point