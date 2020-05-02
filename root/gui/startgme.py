import tkinter as tk
import rs.game as rs

class satup:
    def __init__( self ):
        self.window = tk.Tk()

    def windowset( self ):
        self.window.title( 'Russian Schnapsen - game' )
        self.window.geometry('500x500')
        self.label = tk.Label( self.window )

    def start_game( self ):
        self.playername = self.playernames_input.get()
        if len( self.playername  ) == 0:
            print( 'No name' )
        else:
            print( self.playername )
            players = [ self.playername , 'Dead' ]
            self.coregame = rs.cards( players )
            print( self.coregame.player() )

    def usersname( self ):
        self.windowset()
        usernames_hedline = tk.StringVar()
        usernames = tk.Label(self.window, textvariable = usernames_hedline)
        usernames_hedline.set("Gamer:")
        usernames.pack()
        usernames.place(x= 10, y = 10)

        self.playernames_input = tk.Entry( self.window, width = 50 )
        self.playernames_input.pack()
        self.playernames_input.place(x = 10, y = 30)

        start_play_btn = tk.Button(self.window, text = "Start game", command = self.start_game ) # tworzę przycisk, który będzie wstawiał datę
        start_play_btn.pack()
        start_play_btn.place(x = 10, y = 50)

        tk.mainloop()