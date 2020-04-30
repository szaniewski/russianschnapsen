import rs.game as rs
import tkinter as tk

window = tk.Tk()
window.title( "Russian Schnapsen - game" )
window.geometry('500x500')
label = tk.Label( window )

usersnam = tk.Text( window, width = 100, height = 100 )

tk.mainloop()