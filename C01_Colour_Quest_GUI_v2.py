import tkinter as tk
from tkinter import *
from functools import partial # prevents unwanted windows
import csv
import random

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
            button = Button(self.num_rounds_frame, text=f"{button_info[item][1]} Rounds", font=button_font, bg=button_info[item][0], fg=button_fg, command=lambda i=item: self.to_play(button_info[i][1]))
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

        # variables used to work out statistics when game ends
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # set rounds played and rounds to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        # list to hold scores for stats
        self.user_scores = []
        self.computer_scores = []

        # get all the colours
        self.all_colours = self.get_all_colours()

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        rounds_heading = f"Choose - Round 1 of {how_many}"
        self.choose_heading = Label(self.quest_frame,
            text=rounds_heading, font=("Arial", "16", "bold"))
        self.choose_heading.grid(row=0)
        
        instructions = "Choose one of the colours below. when you choose a colour, the computer's choice and the results for the round will be revealed."
        self.instructions_label = Label(self.quest_frame, text=instructions, wraplength=350, justify="left")
        self.instructions_label.grid(row=1)

        # button_colours_list = self.get_round_colours()
        self.button_colours_list = []

        # create colour buttons
        self.choice_frame = Frame(self.quest_frame)
        self.choice_frame.grid(row=2)

        # list to hold references for coloured buttons so that they can be configured for new rounds
        self.choice_button_ref = []

        for item in range(0, 6):
            self.choice_button = Button(self.choice_frame, 
                                         width=15, command=lambda i=item: self.to_compare(self.button_colours_list[i]))

             
            # add button to reference list for later configuration
            self.choice_button_ref.append(self.choice_button)

            self.choice_button.grid(row=item//3, column=item%3, padx=5, pady=5)

        # display computer choice
        self.comp_choice_label = Label(self.quest_frame, text="Comnputer Choice will appear here", bg="#c0c0c0", width=51)
        self.comp_choice_label.grid(row=3, pady=10)

        # frame to show round results and next button
        self.rounds_frame = Frame(self.quest_frame)
        self.rounds_frame.grid(row=4, pady=5)
        
        self.round_results_label = Label(self.rounds_frame, text=f"Round 1: User - 0  Computer - 0", width=32, bg="#fff2cc", font=("Arial", 10), pady=5)
        self.round_results_label.grid(row=0, column=0, padx=5)

        self.next_button = Button(self.rounds_frame, text="Next Round", fg="#ffffff", bg="#008bfc", font=("Arial", 11, "bold"), width=10, state=DISABLED, command=self.new_round)
        self.next_button.grid(row=0, column=1)

        # at start, get 'new round'
        self.new_round()

        # large label to show overall game results
        self.game_results_label = Label(self.quest_frame, text="Game Totals: User: - \t Computer: - ", width=42, bg="#fff2cc", font=("Arial", 10), padx=10, pady=10)
        self.game_results_label.grid(row=5, pady=5)

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        control_buttons = [
            ["#cc6600", "Help", "get help"],
            ["#004c99", "Statistics", "get stats"],
            ["#808080", "Start Over", "start over"],
            ]

        # so that the text of the 'start over' button can easily be configured when the game is over
        self.control_button_ref = []


        for item in range(0, 3):
            self.make_control_button = Button(self.control_frame, fg="#ffffff", bg=control_buttons[item][0], text=control_buttons[item][1], width=11, font=("Arial", "12", "bold"), command=lambda i=item: self.to_do(control_buttons[i][2]))
            
            self.control_button_ref.append(self.make_control_button)
            
            self.make_control_button.grid(row=0, column=item, padx=5, pady=5)

    # retrieve colours from csv file
    def get_all_colours(self):
        file = open("00_colour_list_hex_v3.csv", "r")
        var_all_colours = list(csv.reader(file, delimiter=","))
        file.close()

        # removes first entry in list (ie. header row)
        var_all_colours.pop(0)
        return var_all_colours

    # randomly choose six colours for buttons
    def get_round_colours(self):
        round_colours_list = []
        colour_scores = []

        # get six unique colours
        while len(round_colours_list) < 6:
            # choose item
            chosen_colour = random.choice(self.all_colours)
            index_chosen = self.all_colours.index(chosen_colour)

            # check score is not already in list
            if chosen_colour[1] not in colour_scores:
                # add item to rounds list
                round_colours_list.append(chosen_colour)
                colour_scores.append(chosen_colour[1])
                
                # remove item from master list
                self.all_colours.pop(index_chosen)
        
        return round_colours_list
    
    def new_round(self):
        # disable next button
        self.next_button.config(state=DISABLED)
        
        # empty colour list for new round
        self.button_colours_list.clear()

        # get new colours for next round
        self.button_colours_list = self.get_round_colours()

        count = 0
        # set button bg, fg, and text
        for item in self.choice_button_ref:
            item["fg"] = self.button_colours_list[count][2]
            item["bg"] = self.button_colours_list[count][0]
            item["text"] = self.button_colours_list[count][0]
            item["state"] = NORMAL
            count += 1

        # retrieve number of rounds and change heading
        how_many = self.rounds_wanted.get()
        current_round = self.rounds_played.get()
        new_heading = f"Choose - Round {current_round+1} of {how_many}"
        self.choose_heading.config(text=new_heading)

    # work out who won and if game is over
    def to_compare(self, user_choice):
        how_many = self.rounds_wanted.get()

        # add one to number of rounds played
        current_round = self.rounds_played.get()
        current_round += 1
        self.rounds_played.set(current_round)

        # deactivate color buttons
        for item in self.choice_button_ref:
            item.config(state=DISABLED)

        # set bg colors
        win_colour = "#d5e8d4"
        lose_colour = "#f8cecc"
        
        # retrieve user score, make it into an integer and add to list for stats
        user_score_current = int(user_choice[1])
        self.user_scores.append(user_score_current)

        # remove user choice from button colours list
        to_remove = self.button_colours_list.index(user_choice)
        self.button_colours_list.pop(to_remove)

        # geet computer choice and add to list for stats
        comp_choice = random.choice(self.button_colours_list)
        comp_score_current = int(comp_choice[1])

        self.computer_scores.append(comp_score_current)

        comp_announce = f"The Computer chose {comp_choice[0]}"

        self.comp_choice_label.config(text=comp_announce, bg=comp_choice[0], fg=comp_choice[2])

        # get colour and show results
        if user_score_current > comp_score_current:
            round_results_bg = win_colour
        else:
            round_results_bg = lose_colour

        rounds_outcome_txt = f"Round {current_round}: User: {user_score_current} \tComputer: {comp_score_current}"

        self.round_results_label.config(bg=round_results_bg, text=rounds_outcome_txt)

        # get total scores for user and computer
        user_total = sum(self.user_scores)
        comp_total = sum(self.computer_scores)

        if user_total > comp_total:
            self.game_results_label.config(bg=win_colour)
            status = "You Win"
        else:
            self.game_results_label.config(bg=lose_colour)
            status = "You Lose"

        game_outcome_txt = f"Total Score: User: {user_total} \tComputer: {comp_total}"

        self.game_results_label.config(text=game_outcome_txt)

        # if the game is over, disable all buttons
        # and change text of "next" button to either "you win" or "you lose" and disable all buttons

        if current_round == how_many:
            # change "next button to show overall win/loss result and disable it"
            self.next_button.config(state=DISABLED, text=status)

            # update "start over button"
            start_over_button = self.control_button_ref[2]
            start_over_button["text"] = "Play Again"
            start_over_button["bg"] = "#009900"

            # change all colour button bg to light gray
            for item in self.choice_button_ref:
                item["bg"] = "#c0c0c0"

        else:
            # enable next round button and update heading
            self.next_button.config(state=NORMAL)

    # detects which 'control' button was pressed and invokes necessary function. can possibly replace functions with calls to classes in this section
    def to_do(self, action):
        if action == "get help":
            self.get_help()
        elif action == "get stats":
            self.get_stats()
        else:
            self.close_play()
    
    def get_stats(self):
        print("You chose to get the statistics")
    
    def get_help(self):
        print("You chose to get help")

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
    