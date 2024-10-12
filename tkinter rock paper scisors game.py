import tkinter as tk
import random

def play_rock_paper_scissors():
    global computer_score, player_score
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    player_choice = choices[choice_var.get()]

    result_label.config(text="")

    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result_label.config (text="Player Won!!!")
        player_score += 1
        player_score_label.config(text=f"Player Score: {player_score}")
    else:
        result_label.config(text="Computer Won!!!")
        computer_score += 1
        computer_score_label.config(text=f"Computer Score: {computer_score}")

    choice_var.set(0)  # Reset player choice

window = tk.Tk()
window.title("Rock Paper Scissors Game")

choice_var = tk.IntVar()
choice_var.set(0)

rock_button = tk.Radiobutton(window, text="Rock", variable=choice_var, value=0)
rock_button.grid(row=1, column=0)

paper_button = tk.Radiobutton(window, text="Paper", variable=choice_var, value=1)
paper_button.grid(row=1, column=1)

scissors_button = tk.Radiobutton(window, text="Scissors", variable=choice_var, value=2)
scissors_button.grid(row=1, column=2)

play_button = tk.Button(window, text="Play", command=play_rock_paper_scissors)
play_button.grid(row=2, column=0, columnspan=3)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=3)

player_score_label = tk.Label(window, text="Player Score: 0")
player_score_label.grid(row=4, column=0)

computer_score_label = tk.Label(window, text="Computer Score: 0")
computer_score_label.grid(row=4, column=2)

player_score = 0
computer_score = 0

window.mainloop()