import rs.game as rs
import tkinter as tk

class satup:
    def __init__( self ):
        self.window = tk.Tk()

    def windowset( self ):
        self.window.title( 'Russian Schnapsen - game' )
        self.window.geometry('500x500')
        self.label = tk.Label( self.window )

    def usersname( self ):
        self.windowset()
        usernames_hedline = tk.StringVar()
        usernames = tk.Label(self.window, textvariable = usernames_hedline)
        usernames_hedline.set("Gamer:")
        usernames.pack()
        usernames.place(x= 10, y = 10)

        usernames_input = tk.Entry( self.window, width = 50, textvariable = usernames_hedline )
        usernames_input.pack()
        usernames_input.place(x = 10, y = 30)

        tk.mainloop()

def main():
    s = satup()
    return s.usersname()

if __name__ == "__main__":
    main()