"""input_requests.py: Secondary user input functions"""


def yesno(question):
    """Yes/no function."""
    ans = input(question).strip().lower()
    while ans not in ["y", "n", ""]:
        ans = input("Please, enter \"y\" or \"n\"").strip().lower()
    if ans == "y":
        return True
    return False


def get_num(low_num=0, high_num=9):
    """Returns an integer between low_num and high_num."""
    while True:
        if low_num == high_num - 1:
            try:
                i_num = int(input("Enter {} or {}: ".format(low_num, high_num)))
                print("")
                assert low_num <= i_num <= high_num
                return i_num
            except ValueError:
                print("Invalid input. Try again.")
        else:
            try:
                i_num = int(input("Enter a number between {} and {}: ".format(low_num, high_num)))
                print("")
                assert low_num <= i_num <= high_num
                return i_num
            except ValueError:
                print("Invalid input. Try again.")


def select_version():
    """Allows player to select which version of the game to play: Classic or Reach"""
    print("""
(1) Classic: An interpretation of the classic board game.
(2) Reach:   A more challenging version with limited feedback.
""")
    return get_num(1, 2)


def change_settings():
    """Change game settings for code length and number of guesses"""
    print("""
CODE LENGTH
The standard code length is 4 digits. 
You can make the game easier by decreasing the number. Or, make it harder by increasing the number.
    """)
    length = get_num(2, 6)

    print("""
GUESS ATTEMPTS
The standard number of guess attempts is 10. 
You can make the game easier by increasing the number. Or, make it harder by decreasing the number.
    """)
    tries = get_num(8, 20)

    return length, tries


