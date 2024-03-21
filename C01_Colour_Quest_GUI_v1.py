import tkinter as tk
from tkinter import *

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

        self.three_button = Button(self.num_rounds_frame,
            fg=button_fg,
            bg="#cc0000", text="3 Rounds",
            font=button_font,
            width=10
            )
        self.three_button.grid(row=0, column=0, padx=5, pady=5)

        self.five_button = Button(self.num_rounds_frame,
            fg=button_fg,
            bg="#009900", text="5 Rounds",
            font=button_font,
            width=10
            )
        self.five_button.grid(row=0, column=1, padx=5, pady=5)

        self.ten_button = Button(self.num_rounds_frame,
            fg=button_fg,
            bg="#000099", text="10 Rounds",
            font=button_font,
            width=10
            )
        self.three_button.grid(row=0, column=2, padx=5, pady=5)


# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Temperature Converter")
    ChooseRounds()
    root.mainloop()