#Jason Johnson
# #100DaysofCode
#Day 22 - Math Game

score = 0
tableChoice = int(input("Choose a multiple for the game: "))

print(f"You chose {tableChoice}! Ready? Set? GO!")

for i in range(1,11,1):
    answer = int(input(f"Round {i}: What is {tableChoice} * {i}:  "))
    if answer == tableChoice * i:
        print ("\033[32mCorrect!\033[0m")
        score += 1
    else:
        print (f"\033[31mIncorrect. The correct answer is \033[0m{tableChoice * i}")    
print()
print(f"\033[33mGame Over! Your Final Score is \033[36m{score}\033[33m.")

if score < 6:
    print("\033[34mBetter Luck Next Time!")
elif score < 10:
    print("\033[32mAlmost Perfect! Great Job!")
elif score == 10: 
    print("\033[36mA PERFECT SCORE!!! YOU ROCK!")
else:
      print("\033[31mI dont underdtand the score... Lets try this again.")

print("\033[0mThanks For Playing!\033[0m")

