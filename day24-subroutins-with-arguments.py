#Jason Johnson
# #replit100DaysofCode
#Day 24 - Subroutines with arguments
#Challenge - Create a subroutine that allows a dice role for an unknow amount of sides 

from random import randint as randroll
def diceRoll(sides):
    while True:
        print(f"You rolled a {randroll(1,sides)}.")
        userChoice = input("Would you like to Roll again? (y/n): ")
        if userChoice == 'y':
            sides = int(input("How many sides does the dice have? "))
            print("restarting")
            continue
        elif userChoice == 'n':
            print ("exiting game")
            print("Thanks for Playing.")
            break
        else:
            print("Unknown command. Exiting Game.")
            exit()

     


''' Test created as I was getting incorrect values. Originally had diceSides = int(input("How many sides does the dice have? "))+1 
which cause and extra side
count = 0
diceSides = int(input("How many sides does the dice have? "))

for i in range(0,100,1):
    roll = diceRoll(diceSides)
    print(f"{roll} / {diceSides}")
    if roll > diceSides:
        count += 1

print(count)

'''
print ("Wlecome to the Dice Roll Generator.")

diceSides = int(input("How many sides does the dice have? "))
diceRoll(diceSides)

