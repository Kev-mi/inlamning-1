import random

def Number_guessing_game(Correct_Number):
    '''Function that asks the user to guess the correct random number'''

    Number_Of_Guesses = 1
    while Correct_Number == False:
        try:
            Guessed_Number = int(input("Guess a random number between 1 and 10"))
            if Guessed_Number == Random_Number:
                print("The number is correct")
                print("It took you " + str(Number_Of_Guesses) + " tries")
                return Number_Of_Guesses
            else:
                Number_Of_Guesses += 1
                if Guessed_Number > Random_Number:
                    print("The number is too large")
                else:
                    print("The number is too small")
        except:
            print("That was not a number!")

def Score_Appender(Score):
    '''Function that takes the amount of guesses as result and adds to a .txt file'''

    Highscore = open("Highscore_Guesses.txt", "a")
    Highscore.write(" %s" % str(Score))
    Highscore.close()

def Number_Guessing_Loop(Want_To_Play):
    '''Function that asks if the user wants to continue to play.'''

    while Want_To_Play == 1:
        Number_Of_Guesses = Number_guessing_game(False)
        Score_Appender(Number_Of_Guesses)
        Want_To_Play = int(input("Type 1 if you want to play again or 0 if you want to quit"))
        if Want_To_Play == 0:
            return None
    return None

def Highscores():
    '''The function if the user wants to see highscores of guesses.
    '''

    Want_To_See = int(input("Type 1 if you want to see highscores"))
    if Want_To_See == 1:
        File = open("Highscore_Guesses.txt", "r")
        Guesses_Highscores = File.read()
        Guesses_Highscores = Guesses_Highscores.split()
        for x in range(0, len(Guesses_Highscores)):
            Guesses_Highscores[x] = int(Guesses_Highscores[x])
        Guesses_Highscores.sort()
        print(Guesses_Highscores)
        File.close()
        return None
    else:
        return None

User_Name = input("What is your name?")
print("Hello " + User_Name)

Random_Number = random.randint(1,10)
Number_Guessing_Loop(1)

Highscores()
