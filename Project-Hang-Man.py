# Final Project Hang Man
# Keegan Killian
# 3.7.19


'''This
is my Final Project for CSSE which is Project-Hang-Man and it is just like normal hang-man.  when start is clicked
the game will chose a random word that you put in the word bank.  The way to win is guess the correct letters without
doing harm to the stick-man.'''


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

        words = ["Destiny", "IT",
                 "Games", "TransFormers", "StephenKing", "food",
                  "NationalLampoonsChristmasVacation", "sleep",
                 "movies","Barneythepurpledinosuar","martialarts",
                 "deadpool", "moo"


                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None # will hold the players guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        joined_word = None # joins the words in the list word_guessed

        HANGMAN = (
'''
------
|    |
|
|
|
|
|
|
---------
''',
'''
------
|    |
|   ( )
|
|
|
|
|
---------
''',
'''
------
|    |
|   ( )
|    |
|
|
|
|
---------
''',
'''
------
|    |
|   ( )
|  /-+-
|
|
|
|
---------
''',
'''
------
|    |
|   ( )
|  /-+-\
|
|
|
|
---------
''',
'''
------
|    |
|   ( )
|  /-+-\
|    |
|
|
|
---------
''',
'''
------
|    |
|   ( )
|  /-+-\
|    |
|   |
|
|
---------
''',
'''
------
|    |
|   ( )
|  /-+-\
|    |
|   |
|   |
|
---------
''',
'''
------
|    |
|   ( )
|  /-+-\
|    |
|   | |
|   |
|
---------
''',
'''
------
|    |
|   ( )
|  /-+-\
|    |
|   | |
|   | |
|
---------
''','''
------
|    |
|   ( )
|  /-+-\
|  | | 
|   | |
|   | |
|
---------
''',
'''
------
|    |
|   ( )
|  /-+-\
|  | | |
|   | |
|   | |
|
---------
''')

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".joined(word_guessed)
            print(joined_word)

            try: