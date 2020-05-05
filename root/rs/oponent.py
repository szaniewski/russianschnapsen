class op:
    def __init__( self, cards ):
        self.figurspowers = cards.get('figur_p')
    def best_choice( self, mycards, openetcard ):
        openetcard = openetcard.split(' ')
        i = 0
        power_best_choice = []
        less_power_best_choice = []

        #Fiding card power
        for f in self.figurspowers:
            if f.find( openetcard[0] ) ==  0:
              opponentcardpower = self.figurspowers.get(f)

        #Create list my card and  power
        for c in mycards['cards']:
            cardname = c.split(' ')[0]
            for p in self.figurspowers:
                if p == cardname:
                    mycards['cards'][i] = [self.figurspowers.get(p) , c]
            i = i + 1

        mycards['cards'].sort()

        #Finde power lest card on heand
        for m in mycards['cards']:
            if m[0] > opponentcardpower:
                power_best_choice.append( m )
                bestchoice = power_best_choice[0]
            else:
                less_power_best_choice.append( m )
                bestchoice = less_power_best_choice[0]
        return bestchoice[1]

#op = op( cards )
#print( op.best_choice( mycards , 'king diamonds') )