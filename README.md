# MastermindIn

**MastermindIn** is a command-line version of the classic Mastermind code breaking game. Instead of colors we are using numbers (0 through 7 inclusive). This is a game where a player tries to guess the number combinations. **MastermindIn** offers a choice of two sets of rules:

### Reach Version

This version follows the rules of the Reach Coding Assignment. 

At the end of each attempt to guess the 4 number combinations, the computer will provide feedback whether the player had guess a number correctly, or/and a number and digit correctly. A player must guess the right number combinations within 10 attempts to win the game.

#### Game rules

* At the start of the game, the computer will randomly select a pattern of four different numbers from a total of 8 different numbers, 0 through 7.
* A player will have 10 attempts to guess the number combinations
* At the end of each guess, computer will provide one of the following response as feedback:
    * The player had guess a correct number
    * The player had guessed a correct number and its correct location
    * The player’s guess was incorrect

Example Run:  
Game initializes and selects "0135"  
Player guesses "2246", game responds "Incorrect"  
Player guesses "0246", game responds "Correct number and location"   
Player guesses "2216", game responds "Correct number"  
...

**The computer’s feedback will not reveal which number the player guessed correctly.

### Classic Version

As an extension to the assignment, I implemented a version that more closely follows the traditional board game.

At the end of each attempt to guess the 4 number combinations, the computer will provide feedback whether the player had guess a number correctly, or/and a number and digit correctly. A player must guess the right number combinations within 10 attempts to win the game.

#### Game rules

* At the start of the game, the computer will randomly select a pattern of four different numbers from a total of 8 different numbers, 0 through 7.
* A player will have 10 attempts to guess the number combinations
* At the end of each guess, computer will provide one of the following response as feedback:
    * "Number & Position": The number of numbers you guessed correctly and in the right location
    * "Number Only":       The number of numbers you guessed correctly (but in the wrong location)

Example Run:   
Game initializes and selects "0135"

Player guesses "2246", game responds:

|Guess     | Number & Position | Number Only |
|-----|-------------------|-------------|
|2246     | 0                 | 0           |

Player guesses "0246", game responds:

|Guess     | Number & Position | Number Only |
|-----|-------------------|-------------|
|2246     | 0                 | 0           |
|0246     | 1                 | 0           |

Player guesses "2216", game responds:

|Guess     | Number & Position | Number Only |
|-----|-------------------|-------------|
|2246     | 0                 | 0           |
|0246     | 1                 | 1           |
|2216     | 0                 | 1           |

Player guesses "2216", game responds:

|Guess     | Number & Position | Number Only |
|-----|-------------------|-------------|
|2246     | 0                 | 0           |
|0246     | 1                 | 0           |
|2216     | 0                 | 1           |
|0153     | 2                 | 2           |

### How to run

* Download repository <https://github.com/Khenu/mastermind.git>.
    * Open Terminal
    * ``git clone <https://github.com/Khenu/mastermind.git>`` to clone the master branch of the repository.
* Run mastermindin.py (located inside mastermind folder, python3).
    * ``cd mastermind`` to cd into the root directory of the repository.
    * ``python3 mastermindin.py`` to start the game.
* Game play instructions are given at the start of the game.

### Thought process and/or code structure

* Thought Process
    * Understand the deliverables and timing (deadline) of this project.
        * Turn instructions into a checklist.
    * Understand the game
        * Not familiar with game. Wikipedia.
        * Understand the rules of the game.
        * User expectations & experience.
        * Write examples of gameplay.
    * Think of a simple way to solve the problem.
        * 1 Generate the pattern
            * Use Random generator API (<https://www.random.org/clients/http/api/)> to randomly select 4 numbers from 0 \~ 7 (Duplicate numbers are allowed)
            * Data structure
                * list, dictionary, other
                * Counter
                    * A mapping that holds an integer count for each key.
                    * Python Counter takes in input a list, tuple, dictionary, string, which are all iterable objects, and it will give you output that will have the count of each element. k, v: key and value
                    * collections.Counter
                * text or int
                    * text because we are not doing any math.
        * 2 Loop through 10 attempts, breaking out the loop when the user select the correct number.
        * For correct number, we want a count of ... Keeping count of "exact guesses" and "close guesses.” Data structure? collections. Counter would work.
            * For exact we need to compare element-wise (iterate in parallel) two lists =\> zip
        * 3 Within the loop
            * Get the guess
            * Analyze the guess
            * Respond to the user
            * Store the response
        * 4 Display the number of guesses remaining
        * 5 Show history
    * User Interface
        * Command line
            * Appropriate for this game
            * "Old school" theme
        * Add extra messages to user
        * ASCII art
* Code Structure
    * The game consists of 4 files:
        * mastermindin.py
        * utils
            * ascii\_art.py
            * input\_requests.py
            * messages.py

### Creative extensions 

* Classic game version
* Ability to select which of the two versions to play
* Ability to customize (length of code, number of guesses
* History of guesses in Classic version
* ASCII art banners
