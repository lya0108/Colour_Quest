import tkinter as tk
from tkinter import *
from functools import partial # prevents unwanted windows

class ChooseRounds:
    def __init__(self) :
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        # GUi frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # heading and instructions
        self.intro_heading = Label(self.intro_frame,
            text="Colour Quest",
            font=("Arial", "16", "bold")
            )
        self.intro_heading.grid(row=0)

        instructions = "Each round you will be given 6 different colours to choose from. Pick a colour and see if you can beat the computer's scoren\n\nTo begin, choose how many rounds you'd like to play..."

        self.intro_instructions = Label(self.intro_frame,
            text=instructions,
            font=("Arial", "12"),
            wraplength=300,
            justify="left"
            )
        self.intro_instructions.grid(row=1)

        # buttons for # of rounds
        self.num_rounds_frame = Frame(self.intro_frame)
        self.num_rounds_frame.grid(row=2)
        
        button_info = [["#cc0000", 3], ["#009900", 5], ["#000099", 10]]
        for item in range(0,3):
            button = Button(self.num_rounds_frame, text=f"{button_info[item][0]} Rounds", font=button_font, bg=button_info[item][1], fg=button_fg, command=lambda i=item: self.to_play(button_info[i][1]))
            button.pack(side=LEFT, padx=5, pady=5)

    def to_play(self, num_rounds):
        Play(num_rounds)
        # hide root window
        root.withdraw()

class Play:
    def __init__(self, how_many):
        self.play_box = Toplevel()

        # if users press cross at top, closes help and release help button
        self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play))

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        rounds_heading = f"Choose - Round 1 of {how_many}"
        self.choose_heading = Label(self.quest_frame,
            text=rounds_heading, font=("Arial", "16", "bold"))
        self.choose_heading.grid(row=0)

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        self.restart_button = Button(self.control_frame, text="Start Over", command=self.close_play)
        self.restart_button.grid(row=0, column=2)

    def close_play(self):
        # reshow root and end current game
        root.deiconify()
        self.play_box.destroy()

# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Colour Quest")
    ChooseRounds()
    root.mainloop()