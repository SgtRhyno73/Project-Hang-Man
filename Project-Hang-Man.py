
game = input("do you want to guess numbers or letters or animals or food or sports or game systems?: ")
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
                 "Games", "StephenKing", "food",
                 "TheFlash", "NationalLampoonsChristmasVacation", "sleep",
                 "movies","Barneythepurpledinosuar", "martialarts",
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
                   "2019", "2020", "2003", "21",
                   "69", "420",
                   "360", "720", "16",
                   "4", "27", "2022", 


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


if game == "animals":
    import random

def main3():
    welcome = ['Welcome to Hangman! A animal will be chosen at random and',
                 'you must try to guess the animal correctly letter by letter',
                 'before you run out of attempts. Good luck!'
                 ]

    for line in welcome:
        print(line)

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        animals = ["cat", "dog",
                   "fox", "hamster", "bear", "honeybadger",
                   "seal", "lizard",
                   "gecko", "bluewhale", "tiger",
                   "spiders"


                   ]

        chosen_animals = random.choice(animals).lower()
        player_guess_animal = None  # will hold the players guess
        guessed_animals = []  # a list of letters guessed so far
        animal_guessed = []
        for animals in chosen_animals:
            animal_guessed.append("-")  # create an unguessed, blank version of the word
        joined_animals = None # joins the words in the list word_guessed

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


        while (attempts != 0 and "-" in animal_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_animals = "".join(animal_guessed)
            print(joined_animals)

            try:
                player_guess_animal = str(input("\nPlease guess a animal" + "\n> ")).lower()
            except:  # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess_animal.isalpha(): # check the input is a number. Also checks an input has been made.
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess_animal) > 1: # check the input is only one number
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess_animal in guessed_animals: # check it number hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_animals.append(player_guess_animal)

            for animals in range(len(chosen_animals)):
                if player_guess_animal == chosen_animals[animals]:
                    animal_guessed[animals] = player_guess_animal # replace all numbers in the chosen word that match your guess

            if player_guess_animal not in chosen_animals:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in animal_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the animal").format(chosen_animals))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The animal was {}.").format(chosen_animals))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if game == "animals":
    main3()

if game == "food":
    import random

def main4():
    welcome = ['Welcome to Hangman! A food item will be chosen at random and',
                 'you must try to guess the food item correctly letter by letter',
                 'before you run out of attempts. Good luck!'
                 ]

    for line in welcome:
        print(line)

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        food = ["bacon", "cookies", "cake", "candy", "brownies", "chocolate",
                "kitkat", "twix", "chicken", "popcornchicken", "wafflefries",


                   ]

        chosen_food = random.choice(food).lower()
        player_guess_food = None  # will hold the players guess
        guessed_food= []  # a list of letters guessed so far
        food_guessed = []
        for food in chosen_food:
            food_guessed.append("-")  # create an unguessed, blank version of the word
        joined_food = None # joins the words in the list word_guessed

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


        while (attempts != 0 and "-" in food_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_food = "".join(food_guessed)
            print(joined_food)

            try:
                player_guess_food = str(input("\nPlease guess a food item" + "\n> ")).lower()
            except:  # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess_food.isalpha(): # check the input is a number. Also checks an input has been made.
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess_food) > 1: # check the input is only one number
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess_food in guessed_food: # check it number hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_food.append(player_guess_food)

            for food in range(len(chosen_food)):
                if player_guess_food == chosen_food[food]:
                    food_guessed[food] = player_guess_food # replace all numbers in the chosen word that match your guess

            if player_guess_food not in chosen_food:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in food_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the food item").format(chosen_food))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The food item was {}.").format(chosen_food))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if game == "food":
    main4()

if game == "sports":
    import random

def main5():
    welcome = ['Welcome to Hangman! A sport will be chosen at random and',
                 'you must try to guess the sport correctly letter by letter',
                 'before you run out of attempts. Good luck!'
                 ]

    for line in welcome:
        print(line)

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        sports = ["archery", "boxing", "fencing", "tennis",
                  "track", "field", "soccer", "pole vault", 
                  "gymnastics", "badminton", "ice hockey", "football", 
                  "volleyball", "baseball", "basketball", "martial arts",


                   ]

        chosen_sports = random.choice(sports).lower()
        player_guess_sports = None  # will hold the players guess
        guessed_sports = []  # a list of letters guessed so far
        sports_guessed = []
        for sports in chosen_sports:
            sports_guessed.append("-")  # create an unguessed, blank version of the word
        joined_sports = None # joins the words in the list word_guessed

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


        while (attempts != 0 and "-" in sports_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_sports = "".join(sports_guessed)
            print(joined_sports)

            try:
                player_guess_sports = str(input("\nPlease guess a sport" + "\n> ")).lower()
            except:  # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess_sports.isalpha(): # check the input is a number. Also checks an input has been made.
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess_sports) > 1: # check the input is only one number
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess_sports in guessed_sports: # check it number hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_sports.append(player_guess_sports)

            for sports in range(len(chosen_sports)):
                if player_guess_sports == chosen_sports[sports]:
                    sports_guessed[sports] = player_guess_sports # replace all numbers in the chosen word that match your guess

            if player_guess_sports not in chosen_sports:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in food_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the sport").format(chosen_sports))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The sport was {}.").format(chosen_sports))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if game == "sports":
    main5()


if game == "game systems":
    import random

def main6():
    welcome = ['Welcome to Hangman! A sport will be chosen at random and',
                 'you must try to guess the sport correctly letter by letter',
                 'before you run out of attempts. Good luck!'
                 ]

    for line in welcome:
        print(line)

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        systems = [


                   ]

        chosen_systems = random.choice(systems).lower()
        player_guess_systems = None  # will hold the players guess
        guessed_systems = []  # a list of letters guessed so far
        systems_guessed = []
        for systems in chosen_systems:
            systems_guessed.append("-")  # create an unguessed, blank version of the word
        joined_systems = None # joins the words in the list word_guessed

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


        while (attempts != 0 and "-" in systems_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_systems = "".join(sysytems_guessed)
            print(joined_systems)

            try:
                player_guess_systems = str(input("\nPlease guess a game system" + "\n> ")).lower()
            except:  # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess_systems.isalpha(): # check the input is a number. Also checks an input has been made.
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess_systems) > 1: # check the input is only one number
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess_systems in guessed_systems: # check it number hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_systems.append(player_guess_systems)

            for systems in range(len(chosen_systems)):
                if player_guess_systems == chosen_systems[systems]:
                    systems_guessed[system] = player_guess_systems # replace all numbers in the chosen word that match your guess

            if player_guess_systems not in chosen_systems:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in systems_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the systems").format(chosen_systems))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The system was {}.").format(chosen_systems))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if game == "game systems":
    main6()


