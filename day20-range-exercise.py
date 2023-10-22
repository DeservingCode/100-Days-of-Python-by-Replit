# Jason Johnson
# #100daysofcode
# Day 20 - Range System based on input

while True:

    lower = int(input("What is the lower limit? "))
    upper = int(input("What is the upper limit? "))
    interval = int(input("what is the interval? "))
    if (lower > upper):
        if (interval >= 0):
            print("Interval will allow for inifite loop. Pleasy try again.")
        else:
            print ("Starting from", lower, "and going to", upper, "with an interval of", interval)
            for i in range(lower, upper, interval):
                print (i)
    if (lower < upper):
        if (interval <= 0):
            print("Interval will allow for inifite loop. Pleasy try again.")
        else:
            print ("Starting from", lower, "and going to", upper, "with an interval of", interval)
            for i in range(lower, upper, interval):
                print (i)

    choice = input("Counter Completed. Would you like to try again? ")
    if choice == 'y':
        continue
    elif choice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Unknown Entry. Ending Program.")
        break