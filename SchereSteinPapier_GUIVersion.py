import random
import tkinter as tk
from tkinter import *

# create window
game = tk.Tk()
game.title("Schere, Stein, Papier")

# global settings

score_handler = {
    "Schere": {"Schere": 1, "Stein": 0, "Papier": 2},
    "Stein": {"Schere": 2, "Stein": 1, "Papier": 0},
    "Papier": {"Schere": 0, "Stein": 2, "Papier": 1},
}
cpu_score = 0
player_score = 0

# game logic and global settings

def outcome_handler(player_choice):
    global cpu_score
    global player_score
    options = ["Stein", "Schere", "Papier"]
    rng = random.randint(0, 2)

    cpu_choice = options[rng]
    result = score_handler[player_choice][cpu_choice]
    lbl_player_choice.configure(
        fg="green", font=("Arial", 8), text="Deine Wahl: " + str(player_choice)
    )
    lbl_cpu_choice.configure(
        fg="red", font=("Arial", 8), text="Der Computer wählt: " + str(cpu_choice)
    )

    if result == 2:
        player_score = player_score + 2
        lbl_player_scores_txt.configure(text="Spieler: " + str(player_score))
        lbl_option_txt.configure(fg="green", text="Du gewinnst!")
    elif result == 1:
        player_score = player_score + 1
        cpu_score = cpu_score + 1
        lbl_player_scores_txt.configure(text="Spieler: " + str(player_score))
        lbl_cpu_scores_txt.configure(text="Computer: " + str(cpu_score))
        lbl_option_txt.configure(fg="blue", text="Unentschieden!")
    elif result == 0:
        cpu_score = cpu_score + 2
        lbl_cpu_scores_txt.configure(text="Computer: " + str(cpu_score))
        lbl_option_txt.configure(fg="red", text="Der Computer gewinnt!")


# labels

lbl_name_txt = tk.Label(game, text="Schere, Stein, Papier", font=("Arial", 14))
lbl_name_txt.grid(row=0, sticky=N, pady=10, padx=200)

lbl_option_txt = tk.Label(
    game, text="Wähle Schere, Stein oder Papier", font=("Arial", 10)
)
lbl_option_txt.grid(row=1, sticky=N)

lbl_player_scores_txt = tk.Label(game, text="Spieler Punkte: 0", font=("Arial", 8))
lbl_player_scores_txt.grid(row=2, sticky=W)

lbl_cpu_scores_txt = tk.Label(game, text="Computer Punkte: 0", font=("Arial", 8))
lbl_cpu_scores_txt.grid(row=2, sticky=E)

lbl_player_choice = tk.Label(game, font=("Arial", 12))
lbl_player_choice.grid(row=3, sticky=W)

lbl_cpu_choice = tk.Label(game, font=("Arial", 12))
lbl_cpu_choice.grid(row=3, sticky=E)

lbl_outcome = tk.Label(game, font=("Arial", 12))
lbl_outcome.grid(row=3, sticky=N)

# buttons

button_rock = tk.Button(
    game, text="Stein", width=15, command=lambda: outcome_handler("Stein")
)
button_rock.grid(row=4, sticky=W, padx=5, pady=5)

button_paper = tk.Button(
    game, text="Papier", width=15, command=lambda: outcome_handler("Papier")
)
button_paper.grid(row=4, sticky=N, padx=5, pady=5)

button_scissor = tk.Button(
    game, text="Schere", width=15, command=lambda: outcome_handler("Schere")
)
button_scissor.grid(row=4, sticky=E, padx=5, pady=5)

# placeholder for grid

lbl_dummy = tk.Label(game)
lbl_dummy.grid(row=5)

game.mainloop()
