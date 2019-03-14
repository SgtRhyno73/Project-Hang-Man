
game = input("do you want numbers or letters?: ")
if game == "letters":
    import random

def main():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!'
               ]

    for line in welcome:
        print(line)

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        words = ["ninjas", "Destiny", "IT",
                 "Games", "TransFormers", "StephenKing", "food",
                 "TheFlash", "NationalLampoonsChristmasVacation", "sleep",
                 "movies","Barneythepurpledinosuar","football", "martialarts",
                 "deadpool"


                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None # will hold the players guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        joined_word = None # joins the words in the list word_guessed

        HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
---------
""",
"""
------
|    |
|   ( )
|
|
|
|
|
|
---------
""",
"""
------
|    |
|   ( )
|    |
|
|
|
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-
|
|
|
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-
|  |
|
|
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  |
|
|
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  |   |
|
|
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
|   
|   
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
|    | 
|   
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
|    | 
|   | 
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
|    | 
|   | 
|   |
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
|    | 
|   | |
|   | 
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
|    | 
|   | |
|   | |
|
---------
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except: # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: # check the input is only one letter
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters: # check it letter hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the word").format(chosen_word))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The word was {}.").format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if game == "letters":
    main()


elif game == "numbers":
    import random

def main2():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
                 'you must try to guess the word correctly letter by letter',
                 'before you run out of attempts. Good luck!'
                 ]

    for line in welcome:
        print(line)

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        numbers = ["10", "15",
                   "2019", "2018", "2003", "21",
                   "69", "420",
                   "360", "720", "16",
                   "4"


                   ]

        chosen_number = random.choice(numbers).lower()
        player_guess_number = None  # will hold the players guess
        guessed_numbers = []  # a list of letters guessed so far
        number_guessed = []
        for numbers in chosen_number:
            number_guessed.append("-")  # create an unguessed, blank version of the word
        joined_number = None # joins the words in the list word_guessed

        HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
<<<<<<< HEAD
|
=======
<<<<<<< HEAD
|
=======
>>>>>>> master
>>>>>>> test-hangman-code
---------
""",
"""
------
|    |
|   ( )
|
|
|
|
|
<<<<<<< HEAD
|
=======
<<<<<<< HEAD
|
=======
>>>>>>> master
>>>>>>> test-hangman-code
---------
""",
"""
------
|    |
|   ( )
|    |
|
|
|
|
<<<<<<< HEAD
|
=======
<<<<<<< HEAD
|
=======
>>>>>>> master
>>>>>>> test-hangman-code
---------
""",
"""
------
|    |
|   ( )
|  /-+-
|
|
|
|
<<<<<<< HEAD
|
=======
<<<<<<< HEAD
|
=======
>>>>>>> master
>>>>>>> test-hangman-code
---------
""",
"""
------
|    |
|   ( )
|  /-+-
|  |
|
|
|
<<<<<<< HEAD
|
=======
<<<<<<< HEAD
|
=======
>>>>>>> master
>>>>>>> test-hangman-code
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  |
|
|
|
<<<<<<< HEAD
|
=======
<<<<<<< HEAD
|
=======
>>>>>>> master
>>>>>>> test-hangman-code
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  |   |
|
|
|
<<<<<<< HEAD
|
=======
<<<<<<< HEAD
|
=======
>>>>>>> master
>>>>>>> test-hangman-code
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
|   
|   
|
<<<<<<< HEAD
|
=======
<<<<<<< HEAD
|
=======
>>>>>>> master
>>>>>>> test-hangman-code
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
<<<<<<< HEAD
|    | 
|   
|
|
=======
<<<<<<< HEAD
|    | 
|   
|
|
=======
|   | 
|   
|
>>>>>>> master
>>>>>>> test-hangman-code
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
<<<<<<< HEAD
|    | 
=======
<<<<<<< HEAD
|    | 
|   | 
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
|    | 
|   | 
|   |
=======
>>>>>>> test-hangman-code
|   | 
|
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
|    | 
|   | 
<<<<<<< HEAD
|   |
=======
>>>>>>> master
>>>>>>> test-hangman-code
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
<<<<<<< HEAD
|    | 
=======
<<<<<<< HEAD
|    | 
=======
>>>>>>> master
>>>>>>> test-hangman-code
|   | |
|   | 
|
---------
""",
"""
------
|    |
|   ( )
|  /-+-\ 
|  | | |
<<<<<<< HEAD
|    | 
=======
<<<<<<< HEAD
|    | 
=======
>>>>>>> master
>>>>>>> test-hangman-code
|   | |
|   | |
|
---------
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "-" in number_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_number = "".join(number_guessed)
            print(joined_number)

            try:
                player_guess_number = str(input("\nPlease select a number between 0-9" + "\n> ")).lower()
            except:  # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess_number.isdigit(): # check the input is a number. Also checks an input has been made.
                    print("That is not a number. Please try again.")
                    continue
                elif len(player_guess_number) > 10: # check the input is only one number
                    print("That is more than one number. Please try again.")
                    continue
                elif player_guess_number in guessed_numbers: # check it number hasn't been guessed already
                    print("You have already guessed that number. Please try again.")
                    continue
                else:
                    pass

            guessed_numbers.append(player_guess_number)

            for number in range(len(chosen_number)):
                if player_guess_number == chosen_number[number]:
                    number_guessed[number] = player_guess_number # replace all numbers in the chosen word that match your guess

            if player_guess_number not in chosen_number:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in number_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the word").format(chosen_number))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The word was {}.").format(chosen_number))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if game == "numbers":
    main2()
else:
    print("I said pick numbers or letters!: ")
