class gameround:
    def __init__(self , tk ):
        self.tk = tk
    def cardonheadn( self, card ):
        pos_start_y = 10
        for c in card:
            self.start_play_btn = tk.Button(self.window, text = c, command = self.carddela )
            self.start_play_btn.pack()
            self.start_play_btn.place(x = 10, y = pos_start_y)
            pos_start_y = pos_start_y + 40
