"""messages.py: Text messages. """


def game_instructions_reach():
    """
    1. Give player game rules.
    2. Get the difficulty by setting the length of the code between 2 and 6 digits.
    3. Get the number of guesses between 8 and 20
    """
    # Print the instructions
    print("""
How to play:
The computer will choose a pattern of four numbers. Each number will be a number between 0 and 7 with 
duplicates allowed.
You will have 10 attempts to guess the number pattern.
After each attempt, the computer will give one of four responses:
    - Incorrect: None of the numbers you guessed appears in the code.
    - Correct number: You guessed one or more numbers but they are in the wrong location
    - Correct number and location: You guessed one or more numbers in the right location
    - You won! You correctly guessed the code.
Enter "q" instead of a guess to quit.
    """)


# TODO Update rules
def game_instructions_classic():
    """
    1. Give player game rules.
    2. Get the difficulty by setting the length of the code between 2 and 6 digits.
    3. Get the number of guesses between 8 and 20
    """
    # Print the instructions
    print("""
How to play:
The computer will choose a pattern of four numbers. Each number will be a number between 0 and 7 with 
duplicates allowed.
You will have 10 attempts to guess the number pattern.
After each attempt, the computer will show:
    - "Number & Position": The number of numbers you guessed correctly and in the right location
    - "Number Only":       The number of numbers you guessed correctly (but in the wrong location)
Enter "q" instead of a guess to quit.
    """)


