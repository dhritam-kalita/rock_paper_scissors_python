# import necessary modules
import random

# define input
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

# assign emojis to inputs
emojis = {
    ROCK: '⛰',
    PAPER: '📃',
    SCISSORS: '✂'
}
# define valid user input
choices = tuple(emojis.keys())

def get_input():
    '''
    function to get valid input from the user
    takes input -> checks validity of input
        -> if valid -> return input
        -> if invalid -> reprompt
    '''
    
    while True:
        user_choice = input("Rock, paper or scissors (r/p/s): ").lower() #get input

        # checks validity of input
        if user_choice not in choices:
            print("Invalid choice!")
            continue
        else:
            return user_choice #returns valid input
        
def display_choices(user_choice, computer_choice):
    '''
    function to print the user's choice and the computer's choice
    '''
    
    print(f"Your choice: {emojis[user_choice]}") #user choice
    print(f"Computer choice: {emojis[computer_choice]}") #computer choice

def find_winners(user_choice, computer_choice):
    '''
    function to determine the winners of the game
    -> checks draw
    -> checks if user wins
    -> else displays computer winner
    '''
    
    # checks draw
    if user_choice == computer_choice:
        print("It is a draw")
        
    # checks if user wins
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print("You won!")
        
    # prints computer as winner
    else:
        print("You lost!")

def do_continue():
    '''
    decides if user wants to continue playing
    '''
    
    if input("Do you want to continue? (y/n): ").lower() == 'n':
        return 0
    else:
        return 1
    
def game():
    '''
    main game loop function
    ->executes all the user defined functions and also decides the choice of the computer
    '''
    
    game = 1
    while game:
        # get user and generate computer choice
        user_choice = get_input()
        computer_choice = random.choice(choices)
        
        display_choices(user_choice, computer_choice) #displays the choices
        
        find_winners(user_choice, computer_choice) #declares winners
        
        game = do_continue()

game() #execution of the game loop function