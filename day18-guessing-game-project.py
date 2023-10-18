#Jason Johnson
#Day 18 of 100
#Build a Number Guessing Game
#100daysofcode by Replit

from random import randint as rando

number = rando(0,100)
attempt = 0
print("----------------------------------------")
print("\033[34mWELCOME TO THE NUMBER GUESSING GAME")
print()
print("\033[35mGuess the number I am thinking of from 0 - 100")
print("\033[35mI will tell you how close your at the guessung the right number")
print()

print("\033[31mReady! \033[33mSET! \033[32mGOOO!!\033[0m")
print("----------------------------------------")

while True:
    attempt += 1
    userGuess = int(input("What is your guess: "))
    if userGuess == number:
        print("You figured it out! I knew you would! ")
        if attempt == 1:
            print("It only took you ONE try?!?!?! Play the lottery today!")
        elif attempt < 5:
            print("It only took you\033[31m", attempt, "\033[0mtries? You're really good at this game!")
        else:
            print("It took you\033[31m", attempt, "\033[0mtries. Play again. I know you can do better!")
        break
    elif userGuess < 0:
        print("Negative Number eneted. Exiting Game...")
        exit()
    elif userGuess < number:
        print("\033[31mNot Quite. Your guess is too low! Try a little higher.\033[0m")
    elif userGuess > number:
        print("\033[32mNot Quite. Your guess is too high! Try a little lower.\033[0m")

    