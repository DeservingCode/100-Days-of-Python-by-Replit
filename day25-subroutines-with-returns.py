#Jason Johnson
# #replit100DaysofCode
#Day 25 - Subroutines with returns
#Challenge - Create a subroutine that allows a dice role for an unknow amount of sides 

from random import randint as randroll
def diceRoll(sides):
    result = randroll(1,sides)
    print (f"Roll = {result}")
    return result

def characterBuilder(name):
    roll = diceRoll(9) * diceRoll(8)
    print(f"You Character Name:")
    if roll % 2 == 0: 
        print(f"{name} the Great! ")
    else:
        print(f"{name} the Terrible! ")

    if roll % 3 == 0:
        print(f"You have the golden stone which give you {roll} + 5 HP. ") 
    elif roll % 2 == 0:
        print(f"You have the silver dagger which give you {roll} - 10 HP. ")
    else:
        print(f"You have {roll} HP.")


print("-- Character Builder Generator --")


while True:
    userName = input("What is your name? ")
    print()
    characterBuilder(userName)
    
    userChoice = input("Would you like to Build another chahrter? (y/n): ")
    if userChoice == 'y':
        print("restarting")
        continue
    elif userChoice == 'n':
        print ("exiting game")
        print("Thanks for Playing.")
        break
    else:
        print("Unknown command. Exiting Game.")
        exit()
