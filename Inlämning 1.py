import random

def yes_or_no(question: str) -> str:
    '''Function that asks the user to answer yes or no and prints out if the user doesn't enter in yes or no.

        Args:
            question(str): the question that the user is going to answer yes or no to.

        Returns:
            user_wish(yes): returns yes or no depending on what the user wants

        '''
    print(question)
    while True:
        user_wish = input()
        if user_wish == "yes":
            return user_wish
        elif user_wish == "no":
            return user_wish
        else:
            print("That was not a yes or no!")

def number_guessing_game() -> int:
    '''Function that asks the user to guess the correct random number

    Args:
        None

    Returns:
        number_of_guesses: integer that points to number of guesses

    '''

    number_of_guesses = 1
    correct_number = False
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


def score_appender(score : int,user_name : str) -> None:
    '''Function that takes the amount of guesses amd user's name as result and adds to a .txt file

    Args:
        score (int): the number of guesses it took the user to answer correctly
        user_name (str) : user's inputed name

    Returns:
        None

    '''

    highscore = open("highscore_guesses.txt", "a")
    highscore.write(user_name + ":"+  "%s " % str(score))
    highscore.close()
    return None


def number_guessing_loop(user_name : str) -> None:
    '''Function that asks if the user wants to continue to play. Also passes on user's name

    Args:
        user_name(str): to pass it on for the number_of_guesses function

    Returns:
        None:

     '''

    want_to_play = "yes"

    while want_to_play == "yes":
        number_of_guesses = number_guessing_game()
        score_appender(number_of_guesses,user_name)
        want_to_play = yes_or_no("Type yes if you want to play again or no if you want to quit")
        if want_to_play == "no":
            return None
    return None


def highscores():
    '''The function if the user wants to see highscores of guesses.

    Args:
        None

    Returns:
        None

    '''

    want_to_see = yes_or_no("Type yes if you want to see highscores, or no and the program will terminate")
    if want_to_see == "yes":
        file = open("Highscore_Guesses.txt", "r")
        guesses_highscores = file.read()
        guesses_highscores = guesses_highscores.split()
        print(guesses_highscores)
        file.close()
        return None
    else:
        return None


user_name = input("What is your name?")
print("Hello" + user_name)

number_guessing_loop(user_name)

highscores()
