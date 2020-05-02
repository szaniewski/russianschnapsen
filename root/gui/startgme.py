import tkinter as tk
import rs.game as rs

class satup:
    def __init__( self ):
        self.playcard = []
        self.window = tk.Tk()

    def characters( self ):
        self.king = tk.PhotoImage( file='gui/gfx/characters/king.gif' )
        return self.king

    def creatcanvas( self ):
        self.can = tk.Canvas( self.window , width=500, height=500 )
        tk.Canvas.create_image(50, 10, characters )

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
            self.creatcanvas()

        print( self.playcard[0].get('cards') )
       # self.cardonheand( self.playcard[0].get('cards') )
        return self.playcard

    def satrtgame( self ):

        self.window.title( 'Russian Schnapsen - game' )
        self.window.geometry('500x500')
        self.label = tk.Label( self.window )

        self.usernames_hedline = tk.StringVar()
        self.usernames = tk.Label( self.window, textvariable =self.usernames_hedline )
        self.usernames_hedline.set("Gamer:")
        self.usernames.pack()
        self.usernames.place(x= 10, y = 10)

        self.playernames_input = tk.Entry( self.window, width = 50 )
        self.playernames_input.pack()
        self.playernames_input.place(x = 10, y = 30)

        self.start_play_btn = tk.Button(self.window, text = "Start game", command = self.carddela )
        self.start_play_btn.pack()
        self.start_play_btn.place(x = 10, y = 50)
        tk.mainloop()

    def selectedcard( self, cardname):
        self.selected = cardname
        print( self.selected )
        return self.selected