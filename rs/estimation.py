import random

class cards:

    def __init__( self ):
        self.playerheand = []
        self.gams_card = []
        self.cardonstck = []
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
        for card in list( self.cards['figur_p'].keys() ):
            for color in list( self.cards['marriage_p'].keys() ):
                self.gams_card.append( card + ' ' + color )
        return self.gams_card

    def shuffling( self ):
        """
        First hend cards
        """
        random.shuffle( self.gams_card )
        self.playerheand += [self.gams_card[:self.gamesruls['heand']]]
        self.playerheand += [self.gams_card[self.gamesruls['heand']:]]
        self.cardonstck = self.gams_card[self.gamesruls['heand'] * 2:]