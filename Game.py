import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):  # Change _init_ to __init__
        self.master = master
        master.title("Rock, Paper, Scissors")

        self.user_choice = None
        self.computer_choice = None
        
        self.user_label = tk.Label(master, text="Choose Rock, Paper or Scissors")
        self.user_label.pack()

        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play("Rock"))
        self.rock_button.pack()

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play("Paper"))
        self.paper_button.pack()

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors_button.pack()

        self.result_label = tk.Label(master, text="", font=("Arial", 16))
        self.result_label.pack()

    def play(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.determine_winner()

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            result = "It's a tie!"
        elif (self.user_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.user_choice == "Paper" and self.computer_choice == "Rock") or \
             (self.user_choice == "Scissors" and self.computer_choice == "Paper"):
            result = "You win!"
        else:
            result = "You lose!"

        self.result_label.config(text=f"You chose {self.user_choice}, Computer chose {self.computer_choice}. {result}")

if __name__ == "__main__":  # Corrected this line
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
