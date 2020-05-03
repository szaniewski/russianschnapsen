import tkinter as tk
import rs.game as rs
from PIL import ImageTk, Image

class satup:
    def __init__( self ):
        self.playcard = []

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

    def select_card( self, c ):
        print('selecterd', c)

    def cardonheadn( self, card ):
        pos_start_x = 10
        self.character_king = tk.PhotoImage(file='gui/gfx/characters/king.gif')

        for c in card:
            self.start_play_btn = tk.Button(self.window,  text = c, image=self.character_king, command = lambda:self.select_card( c ),  borderwidth = 0)
            self.start_play_btn.pack()
            self.start_play_btn.place(x = pos_start_x, y = 350 )
            pos_start_x = pos_start_x + 80