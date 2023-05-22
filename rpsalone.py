import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")

player_score = 0
high_score = 0

def play(player_choice):
    global player_score, high_score

    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)
    if (player_choice == comp_choice):
        result = "Tie!"
    elif (
        (player_choice == "Rock" and comp_choice == "Scissors") or
        (player_choice == "Paper" and comp_choice == "Rock") or
        (player_choice == "Scissors" and comp_choice == "Paper")
    ):
        result = "You win!"
        player_score += 1
    else:
        result = "You lost.."
        if(high_score<player_score):
            high_score = player_score
        messagebox.showinfo("Game Over", "You scored " + str(player_score) + "\n High Score : " + str(high_score))
        player_score = 0

    update_scores(player_score, high_score)
    show_result(player_choice, comp_choice, result)

def update_scores(player_score, high_score):
    player_score_label.config(text="Player Score : " + str(player_score))
    high_score_label.config(text="High Score : " + str(high_score))
    
    
result_label = tk.Label(root, text="")
result_label.pack()

def show_result(player_choice, comp_choice, result):
    if result == "Tie!":
        message = "Your {} tied".format(player_choice)
    elif result == "You win!":
        message = "Your {} won".format(player_choice)
    elif result == "You lost..":
        message = "Your {} got beaten".format(player_choice)
    
    result_label.config(text= message +"\nComputer: " + comp_choice + "\nResult: " + result)

player_score_label = tk.Label(root, text="Player Score : 0")
player_score_label.pack()

high_score_label = tk.Label(root, text="High Score : 0")
high_score_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()


## Button

rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"))
rock_button.pack(side="left", fill="x", expand=True, padx=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"))
paper_button.pack(side="left", fill="x", expand=True, padx=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))
scissors_button.pack(side="left", fill="x", expand=True, padx=10)

root.mainloop()