#Jason Johnson
#Day 18 of 100
#Build a Number Guessing Game
#100daysofcode by Replit

from random import randint as rando

number = rando(0,100)
attempt = 0

print("\033[196;256mWELCOME TO THE NUMBER GUESSING GAME\033[0m")
print("Guess the number I am thinking of from 0 - 100")
print("I will tell you how close your at the guessung the right number")

print("Ready! SET! GOOO!!")
while True:
    attempt += 1
    userGuess = int(input("What is your guess: "))
    if userGuess == number:
        print("You figured it out! I knew you would! ")
        if attempt == 1:
            print("It only took you ONE try?!?!?! Play the lottery today!")
        elif attempt < 10:
            print("It only took you", attempt, "tries? You're really good at this game!")
        else:
            print("It took you", attempt, "tries. Play again. I know you can do better!")
        break
    elif userGuess < 0:
        print("Negative Number eneted. Exiting Game...")
        exit()
    elif userGuess < number:
        print("Not Quite. Your guess is too low! Try a little higher.")
    elif userGuess > number:
        print("Not Quite. Your guess is too high! Try a little lower.")

    