import tkinter as tk
import rs.game as rs
from PIL import ImageTk, Image

class satup:
    def __init__( self ):
        self.playcard = []
        self.card_value = {}

    def carddela( self ):
        self.playername = self.playernames_input.get()
        if len( self.playername  ) == 0:
            print( 'No name' )
        else:
            players = [ self.playername , 'Dead' ]
            self.coregame = rs.cards( players )
            self.playcard = self.coregame.player()
            self.usernames.destroy()
            self.playernames_input.destroy()
            self.start_play_btn.destroy()

        self.cardonheadn( self.playcard[0].get('cards') )
        return self.playcard

    def satrtgame( self ):

        self.window = tk.Tk()
        self.window.title( 'Russian Schnapsen - game' )
        self.window.geometry('850x500')
        self.label = tk.Label( self.window )

        self.usernames_hedline = tk.StringVar()
        self.usernames = tk.Label( self.window, textvariable =self.usernames_hedline )
        self.usernames_hedline.set('Gamer:')
        self.usernames.pack()
        self.usernames.place(x= 10, y = 10)

        self.playernames_input = tk.Entry( self.window, width = 50 )
        self.playernames_input.pack()
        self.playernames_input.place(x = 10, y = 30)

        self.start_play_btn = tk.Button(self.window, text = 'Start game', command = self.carddela )
        self.start_play_btn.pack()
        self.start_play_btn.place(x = 10, y = 50)
        tk.mainloop()

    def select_card( self, i, c ):
        self.card_value = {'id': i, 'name': c }
        print( self.card_value )

    def cardonheadn( self, card ):
        i = 0
        self.character = tk.PhotoImage(file='gui/gfx/characters/dragon/Idle1.png')
        self.character_dragon = tk.PhotoImage(file='gui/gfx/characters/dragon/Idle1.png')
        self.character_demon = tk.PhotoImage(file='gui/gfx/characters/demon/Idle1.png')
        self.character_medusa = tk.PhotoImage(file='gui/gfx/characters/medusa/Idle1.png')
        self.character_lizard = tk.PhotoImage(file='gui/gfx/characters/lizard/Idle1.png')
        self.character_jinn = tk.PhotoImage(file='gui/gfx/characters/jinn/Idle1.png')
        self.character_small_dragon = tk.PhotoImage(file='gui/gfx/characters/small_dragon/Idle1.png')
        self.cards_btn = {}

        for c in card:
            print( c )
            if c.find('ass') == 0:
                self.character = self.character_dragon
            elif c.find('king') == 0:
                self.character = self.character_demon
            elif c.find('ten') == 0:
                self.character = self.character_jinn
            elif c.find('ober') == 0:
                self.character = self.character_medusa
            elif c.find('unter') == 0:
                self.character = self.character_lizard
            elif c.find('nine') == 0:
                self.character = self.character_small_dragon

            self.cards_btn[i]= tk.Button( self.window, text = c, image=self.character, command = lambda: self.select_card(i, c),  borderwidth = 0 )
            self.cards_btn[i].grid( row = 10, column = i , pady = 1 )
            i = i + 1




