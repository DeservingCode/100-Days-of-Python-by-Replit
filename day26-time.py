import time, os

def textDelay(line1,line2,line3,delay1):
    os.system("clear")
    print(line1)
    time.sleep(delay1)
    print(line2)
    time.sleep(delay1)
    print(line3)
    time.sleep(delay1*2)

while True:
    
    textDelay("Welcome to The iZune Player","Created in 2023, Born in 1995","Deserving Code",1)
    print("""
          
""")
    print("Please enter your selection:")
    print("1 - for Music")
    print("2 - for Settings")
    print("3 - Quit")
    time.sleep(.5)
    userChoice = int(input("Please make a selection: "))

    if userChoice == 1:
        print("Now Loading Music")
        time.sleep(.5)
        print("Music playing")
        time.sleep(1)
        print("Restarting")
        time.sleep(.5)



    elif userChoice == 2:
        os.system("clear")
        print("User Settings: ")
        print("1 - Device Serial")
        print("2 - Volume")
        print("3 - Go Back")
        time.sleep(5)


    elif userChoice == 3:
        exit()

    else:
        print("invalid command. Please try again")

