import random

emojis = {
    'r': '⛰',
    'p': '📃',
    's': '✂'
}
choices = ('r', 'p', 's')

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
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')
    ):
        print("You won!")
    else:
        print("You lost!")
        