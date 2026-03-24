import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {
    ROCK: '⛰',
    PAPER: '📃',
    SCISSORS: '✂'
}
choices = (ROCK, PAPER, SCISSORS)

while True:
    user_choice = input("Rock, paper or scissors (r/p/s): ").lower()

    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f"Your choice: {emojis[user_choice]}")
    print(f"Computer choice: {emojis[computer_choice]}")
    
    if user_choice == computer_choice:
        print("It is a draw")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print("You won!")
    else:
        print("You lost!")
        