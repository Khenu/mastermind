"""mastermindin.py: Mastermind game."""


import collections
import requests
import signal
import asyncio
from utils.input_requests import yesno, change_settings, select_version
from utils.messages import game_instructions_reach, game_instructions_classic
from utils.ascii_art import title_banner, gameover_banner, youwon_banner









def get_guess(c_length) -> str:
    """Get guess from the player."""
    while True:

        player_input = input("\nEnter {} integers between 0 and 7 (without spaces): ".format(c_length))
        print("")

        # Process quit command
        if player_input.lower() == "q":
            return "q"

        # Check if the input is a valid guess
        if len(player_input) == c_length and "8" not in player_input and "9" not in player_input:
            return player_input
        else:
            print("Invalid input. Try again.")





def alarm_handler(signum, frame):
    """called when read times out"""
    print('Time\'s up!')


# Register the alarm signal with our handler
signal.signal(signal.SIGALRM, alarm_handler)


def get_input():
    try:
        print('You have 60 seconds to type in your guess')
        foo = raw_input()
        return foo
    except:
        # timeout
        return


# set alarm to TIMEOUT seconds
signal.alarm(TIMEOUT)
s = get_input()
# disable the alarm after success
signal.alarm(0)
print('You typed', s)








def evaluate_guess_linkedin(code2break, guess4code):
    """
    Evaluate the guess and respond to the player with one of the following:
    1. Correct number and location
    2. Correct number
    3. Incorrect
    *Assumption: If both 'Correct number and location' and 'Correct number', reply with 'Correct number and location'
    """

    # Determine the number of exact matches (number and position)
    num_exact = sum(a == b for a, b in zip(code2break, guess4code))

    # Determine the number of close matches (number only)
    pattern_counted = collections.Counter(code2break)
    guess_counted = collections.Counter(guess4code)
    # "close" matches include "exact" matches. To get "close only" matches, subtract exact matches
    num_close = sum(min(pattern_counted[k], guess_counted[k]) for k in pattern_counted) - num_exact

    # Give feedback to player
    if num_exact:
        print('Correct number and location')
    elif num_close:
        print('Correct number')
    else:
        print('Incorrect')

    return num_exact == len(code2break)


def evaluate_guess_classic(code2break, guess4code):
    """
    Evaluate the guess and respond to the player with the number of:
    correct number and location
    correct number
    """
    # Determine the number of exact matches (number and location)
    num_exact = sum(a == b for a, b in zip(code2break, guess4code))

    # Determine the number of close matches (number only)
    pattern_counter = collections.Counter(code2break)
    guess_counter = collections.Counter(guess4code)
    # "close" matches include "exact" matches. To get "close only" matches, subtract exact matches
    num_close = sum(min(pattern_counter[k], guess_counter[k]) for k in pattern_counter) - num_exact

    # guess is correct
    full_match = num_exact == len(code2break)

    return full_match, num_exact, num_close


def get_random_code(num) -> str:
    """Get random number of length num from random.org"""
    source = "https://www.random.org/integers/?num={}&min=0&max=7&col=1&base=10&format=plain&rnd=new".format(num)
    response = requests.get(source)               # get returns a column
    num_str_list = response.text.splitlines()     # text is a property
    number_text = "".join(num_str_list)
    return number_text


def print_history(hist):
    """Print history of gameplay in columns"""
    # Find lengths of row elements
    length_list = [len(element) for row in hist for element in row]
    # Longest element sets column_width
    column_width = max(length_list)
    # Print elements with even spacing
    for row in hist:
        print("".join(element.ljust(column_width + 2) for element in row))
    print("")


# Game play defaults
code_length = 4
num_guesses = 10
timeout = 60


# Game play history for Classic version
history = [["Guess", "Number & Position", "Number Only"]]

# Display title banner
title_banner()

# Select version of the game
ver = select_version()

# Give the user gameplay instructions
game_instructions_classic() if ver == 1 else game_instructions_reach()

# Ask player to start game or change difficulty
if yesno("Press Enter to play. \nOr, enter \"y\" to change the difficulty (code length and/or number of tries)."):
    code_length, num_guesses = change_settings()
else:
    print("OK. We\'ll use the defaults: code length of {} and {} guesses.\n".format(code_length, num_guesses))

# Generate code for game
pattern = get_random_code(code_length)

# Play game until player wins or exhausts attempts
for attempt in range(num_guesses):

    # Get player's guess or quit command
    guess = get_guess(code_length, timeout)

    # Execute quit command
    if guess == "q":
        gameover_banner()
        print('The code was {}. Thanks for playing!\n'.format(''.join(pattern)))
        break

    # Evaluate guess
    exacts = closes = 0
    if ver == 1:
        won, exacts, closes = evaluate_guess_classic(pattern, guess)
    else:
        won = evaluate_guess_linkedin(pattern, guess)

    if won:
        youwon_banner()
        print('Congratulations!\n')
        break
    # Classic version: Save guess to history and print
    elif ver == 1:
        history.append([guess, str(exacts), str(closes)])
        print_history(history)

    # Show remaining number of guesses
    print('{} guesses remaining:'.format(num_guesses - 1 - attempt))

else:  # When the for completes normally (not by a break)
    gameover_banner()
    print('You have exhausted your attempts. The code was {}.\n'.format(''.join(pattern)))


