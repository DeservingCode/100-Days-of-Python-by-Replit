#Jason Johnson
# #100DaysofCode
#Day 23 - Subroutines AKA Functions? 
#Challenge - Create a subroutine thats asks for username and password. It keeps looping until correct data entered. 
websitelogin = False
def loginCheck():
    username = input("Enter User Name: ")
    password = input("Enter password: ")

    if username == "admin101" and password == "hello12345":
        print("\33[32mLogin Correct\33[0m")
        return True
    else:
        print("\33[31mIncorrect Login\33[0m")
        return False
    
while websitelogin == False:
    
    websitelogin = loginCheck()
