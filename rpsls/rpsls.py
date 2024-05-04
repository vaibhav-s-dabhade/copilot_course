# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock
# - Rock crushes lizard
# - Lizard poisons Spock
# - Spock smashes scissors
# - Lizard eats paper
# - Paper disproves Spock
# - Spock vaporizes rock
# - Rock crushes scissors
# Include user input for selecting options and display game results

import random

def rpsls():
    # Define game options
    options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    # Define game rules
    rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    # Get user input
    user_input = input('Enter your choice (rock, paper, scissors, lizard, spock): ').lower()

    # Validate user input
    if user_input not in options:
        print('Invalid input. Please try again.')
        return

    # Get computer choice
    computer_choice = random.choice(options)

    # Determine game result
    if user_input == computer_choice:
        print(f'Computer chose {computer_choice}. It\'s a tie!')
    elif computer_choice in rules[user_input]:
        print(f'Computer chose {computer_choice}. You win!')
    else:
        print(f'Computer chose {computer_choice}. You lose!')

if __name__ == '__main__':
    rpsls()

    
