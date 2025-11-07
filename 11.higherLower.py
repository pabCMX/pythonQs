from random import randint
import time

compRand = randint(0, 100)
usrTurn = False
compGuess = randint(0,100)
hiRange = 100
loRange = 0
usrGuess = 0
guessTotal = 0
numCorrect = False
turnIn = input("Would you like to guess first? Y/N: ")
gameContinue = True

if turnIn == "Y" or turnIn == "y":
        usrTurn = True

while gameContinue:
    if not usrTurn:
        print("Think of a number!")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("!")
        while not numCorrect:
            usrCorrect = input("Comp guesses {}, is that correct (C), high (H) or low(L)? C/H/L: ".format(compGuess))
            if usrCorrect == "C" or usrCorrect == "c":
                numCorrect = True
                usrTurn = True
                loRange = 0
                hiRange = 100
                guessTotal+=1
            elif usrCorrect == "H" or usrCorrect == "h":
                hiRange = compGuess
                compGuess = int((loRange+hiRange)/2)
                guessTotal+=1
            elif usrCorrect == "L" or usrCorrect == "l":
                loRange = compGuess
                compGuess = int((loRange+hiRange)/2)
                guessTotal+=1
            else:
                print("Try again, that was an invalid answer.")
        print("Great! it took {} guesses!".format(guessTotal))
    else:
        print("Thinking of a number...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("Done!")
        while not numCorrect:
            usrGuess = int(input("What is your guess? "))
            if usrGuess == compRand:
                numCorrect = True
                usrTurn = False
                guessTotal+=1
            elif usrGuess > compRand:
                print("Too high")
                guessTotal+=1
            elif usrGuess < compRand:
                print("Too low")
                guessTotal+=1
        print("Great! it took {} guesses!".format(guessTotal))
    usrContinue = input("Would you like to continue playing? Y/N ")
    if usrContinue == "N" or usrContinue == "n":
        gameContinue = False         
    elif usrContinue == "Y" or usrContinue == "y":
        numCorrect = False
        guessTotal = 0
        print("Comp turn to guess!")
    else:
        print("Invalid Answer, exiting")
        gameContinue = False
time.sleep(0.25)
print("Thanks for playing!")
time.sleep(0.5)
print("Shutting down")