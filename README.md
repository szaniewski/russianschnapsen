# Russuan Schnapsen - game

# Status / Version
Development (Beta) / 0.1.5

Desktop game screen

![picture](http://roch.lh.pl/git/russuan_schnapsen/hallo.png | width=100)
![picture](http://roch.lh.pl/git/russuan_schnapsen/card.png | width=100)
![picture](http://roch.lh.pl/git/russuan_schnapsen/character.png | width=100)

# Russian Schnapsen - module
Estymiation Yours card in Russian Schnapsen https://en.wikipedia.org/wiki/Russian_Schnapsen


# Status / Version
Development (Beta) / 0.2.5

# how to use
```Python
#import module
import rs.game as rs

#Start gemse 
# @playernams - arr names of player
playernames = ['Adam', 'Ola']
c = rs.cards( playernames )

print( c.player() )

# Return exemp "data"
# Last element on dic is "mus" (gams rools)
{'player': 'Adam', 'cards': ['king diamonds', 'king pikes', 'unter pikes', 'nine pikes', 'ten diamonds', 'ober pikes', 'nine clubs', 'ten pikes', 'king clubs', 'nine hearts'], 'points': [117]}, {'player': 'Ola', 'cards': ['ass pikes', 'ass diamonds', 'ass hearts', 'ober diamonds', 'unter clubs', 'nine diamonds', 'ten hearts', 'unter diamonds', 'king hearts', 'ass clubs'], 'points': [102]}, {'cards': ['unter hearts', 'ober clubs', 'ten clubs'], 'points': [37]}

#opposing cards
opponents = ['nine pikes', 'ten diamonds']

#who win
print( c.winers(opponents) )

#return winer name
'Adam'

# Computer play - select best card on headn

computer_card = {'player': 'Cat', 'cards': ['ober hearts', 'ten diamonds', 'king clubs', 'unter hearts', 'ass diamonds', 'ass pikes', 'ober clubs', 'nine hearts', 'nine diamonds', 'ober pikes'], 'points': [94]}

print( c.autoplay(computer_card, 'ass pikes') )

# Resonce
'nine diamonds'
```
