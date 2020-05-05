import tkinter as tk
import rs.game as rs
from PIL import ImageTk, Image
class satup:
    def __init__( self ):
        self.playcard = []
        self.cards_btn = []

    def carddela( self ):
        self.playername = self.playernames_input.get()
        if len( self.playername  ) == 0:
            print( 'No name' )
        else:
            self.players = [ self.playername , 'Dead' ]
            self.coregame = rs.cards( self.players )
            self.playcard = self.coregame.player()

            self.usernames.destroy()
            self.playernames_input.destroy()
            self.start_play_btn.destroy()
            self.usernames.destroy()
            self.bgintro.destroy()

        self.cardonheadn( self.playcard[0].get('cards') )

        return self.playcard

    def stage_intro( self ):
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

    def satrtgame( self ):

        self.window = tk.Tk()
        self.window.title( 'Russian Schnapsen - game' )
        self.window.geometry('500x500')
        self.label = tk.Label( self.window )

        self.bg = tk.PhotoImage( file='gui/gfx/bg_retro.gif' )
        self.bgintro = tk.Label( self.window, image = self.bg )
        self.bgintro.pack()
        self.bgintro.pack(side='top', fill='both', expand='yes')

        # self.bechemotcat_img = tk.PhotoImage( file='gui/gfx/demon.gif' )
        # self.bechemotcat = tk.Label( self.window, image = self.bechemotcat_img )
        # self.bechemotcat.pack()
        # self.bechemotcat.pack(side='top', fill='both', expand='yes')

        self.window.after( 1000, self.stage_intro )
        tk.mainloop()

    def select_card( self, i, c ):
        card_selected = c
        card_id = i
        self.cards_btn[ card_id ].config( borderwidth = 1 )
        self.skirmisch( card_selected )
        return card_selected

    def cardonheadn( self, card ):
        self.window.geometry('800x500')
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
            ctr = lambda i = i, c = c:  self.select_card(i, c)
            self.cards_btn[i]= tk.Button( self.window, text = c, image=self.character, command = ctr,  borderwidth = 0 )
            self.cards_btn[i].grid( row = 10, column = i , pady = 10 )
            i = i + 1

    def skirmisch( self, card_selected ):
        computer_card = self.coregame.autoplay( self.playcard[1], card_selected )
        print( computer_card )
        return computer_card



