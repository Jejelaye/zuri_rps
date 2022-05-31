from random import random
from math import floor

possible_options = ['R', 'P', 'S']
print('''
    Welcome to the rock, paper, scissors game.
    Please choose either rock (r), paper (p)
    or scissors (s) to start playing.        
''')


def human():
    human_choice: str = input('''
        Write your choice here >>>: 
    ''').upper()

    if human_choice not in possible_options:
        print('''
        Come on, you\'re smarter than that.
        Choose again
        ''')
        return human()
    else:
        return human_choice


def computer():
    return possible_options[floor(random() * len(possible_options))]


def compare_answers(player, cpu):
    if player == cpu:
        print(f"Both players selected {player}. It's a tie!")
    elif player == 'R':
        if cpu == 'S':
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == 'P':
        if cpu == 'R':
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player == 'S':
        if cpu == 'P':
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


def rps_init():
    player_choice = human()
    cpu_choice = computer()

    compare_answers(player_choice, cpu_choice)
    print(f'Player ({player_choice}) : CPU ({cpu_choice})')


# print(f'Player ({player_choice}) : CPU ({cpu_choice})')

rps_init()
