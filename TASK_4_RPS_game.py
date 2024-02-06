import tkinter as tki
import random

root = tki.Tk()
root.title("Rock Paper Scissors")

user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    result_message = (
        f"Your choice: {user_choice.capitalize()}\n"
        f"Computer's choice: {computer_choice.capitalize()}\n"
    )

    if user_choice == computer_choice:
        result_message += "It's a tie!"
        result_label.config(fg="gray")  # Change text color for tie
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        result_message += "You win!"
        user_score += 1
        result_label.config(fg="green")  # Change text color for win
    else:
        result_message += "You lose!"
        computer_score += 1
        result_label.config(fg="red")  # Change text color for lose

    result_label.config(text=f"Result: {result_message}")
    score_label.config(text=f"Your Score: {user_score}, Computer's Score: {computer_score}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")
    user_choice_label.config(text=f"Your Choice: {user_choice.capitalize()}")

# Function to display instructions
def display_instructions():
    result_label.config(text="Click Rock, Paper, or Scissors to play!")

rock_button = tki.Button(root, text="Rock", command=lambda: [play_game('rock'), display_instructions()], padx=20, pady=10)
rock_button.pack(side=tki.LEFT, padx=10)

paper_button = tki.Button(root, text="Paper", command=lambda: [play_game('paper'), display_instructions()], padx=20, pady=10)
paper_button.pack(side=tki.LEFT, padx=10)

scissors_button = tki.Button(root, text="Scissors", command=lambda: [play_game('scissors'), display_instructions()], padx=20, pady=10)
scissors_button.pack(side=tki.LEFT, padx=10)

result_label = tki.Label(root, text="Click Rock, Paper, or Scissors to play!", font=("Helvetica", 12))
result_label.pack(pady=10)

user_choice_label = tki.Label(root, text="", font=("Helvetica", 12))
user_choice_label.pack()

computer_choice_label = tki.Label(root, text="", font=("Helvetica", 12))
computer_choice_label.pack()

score_label = tki.Label(root, text="", font=("Helvetica", 12))
score_label.pack()

root.mainloop()
