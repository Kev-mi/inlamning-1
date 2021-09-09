import random


def number_guessing_game(correct_number: int) -> int:
    '''Function that asks the user to guess the correct random number

    Args:
        correct_number(int): the randomly generated number that the user is asked to guess

    Returns:
        number_of_guesses: integer that points to number of guesses

    '''

    number_of_guesses = 1
    random_number = random.randint(1, 10)
    while correct_number == False:
        try:
            guessed_number = int(input("Guess a random number between 1 and 10"))
            if guessed_number == random_number:
                print("The number is correct")
                print("It took you " + str(number_of_guesses) + " tries")
                return number_of_guesses
            else:
                number_of_guesses += 1
                if guessed_number > random_number:
                    print("The number is too large")
                else:
                    print("The number is too small")
        except ValueError:
            print("That was not a number!")


def score_appender(score: int) -> None:
    '''Function that takes the amount of guesses as result and adds to a .txt file

    Args:
        score (int): the number of guesses it took the user to answer correctly

    Returns:
        None

    '''

    highscore = open("highscore_guesses.txt", "a")
    highscore.write(" %s" % str(score))
    highscore.close()
    return None


def number_guessing_loop(want_to_play: int) -> None:
    '''Function that asks if the user wants to continue to play.

    Args:
        Want_To_Play (int): int that determines if user wants to play

    Returns:
        None:

     '''

    want_to_play = 1

    while want_to_play == 1:
        number_of_guesses = number_guessing_game(False)
        score_appender(number_of_guesses)
        want_to_play = int(input("Type 1 if you want to play again or 0 if you want to quit"))
        if want_to_play == 0:
            return None
    return None


def highscores():
    '''The function if the user wants to see highscores of guesses.

    Args:
        None

    Returns:
        None

    '''

    want_to_see = int(input("Type 1 if you want to see highscores, otherwise the program will terminate"))
    if want_to_see == 1:
        file = open("Highscore_Guesses.txt", "r")
        guesses_highscores = file.read()
        guesses_highscores = guesses_highscores.split()
        for x in range(0, len(guesses_highscores)):
            guesses_highscores[x] = int(guesses_highscores[x])
        guesses_highscores.sort()
        print(guesses_highscores)
        file.close()
        return None
    else:
        return None


user_name = input("What is your name?")
print("Hello " + user_name)

number_guessing_loop()

highscores()
