class roolsgame:
    def __init__( self, shuffling ):
        self.nine = 0
        self.shuffling = shuffling
        self.restart = False

    def finding_nines( self ):
        #4 nines on head
        for i in range(2):
            for c in self.shuffling[i]:
                if c.find('nine') == 0:
                    self.nine =  self.nine + 1
            if self.nine == 4:
                self.restart = True
            else:
                self.nine = 0
        #2 nines on "MUS"
        for m in self.shuffling[2]:
            if m.find('nine') == 0:
                self.nine =  self.nine + 1
        if self.nine == 2:
            self.restart = True
        else:
            self.nine = 0

        return self.restart