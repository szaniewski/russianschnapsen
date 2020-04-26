import random

cards = {
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

gamesruls = {
    'heand': 10,
    'stos': 4
}

gams_card = []
player_one = []
player_two = []

"""
The deck
"""
for card in list(cards['figur_p'].keys()):
    for color in list(cards['marriage_p'].keys()):
        gams_card.append( card + ' ' + color )

"""
First hend cards
"""

player_one.append( random.choices( gams_card, k=gamesruls['heand'] ) )

for i in player_one[0]:
    if i in gams_card:
        gams_card.remove(str(i))

print( gams_card )
print( len(gams_card) )
