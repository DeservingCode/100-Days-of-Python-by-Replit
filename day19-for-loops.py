#Jason Johnson
#100 Days of Code 
# Day 19

print("Loan Calculator")
print()
loanAmount = int(input("Enter Loan Amount: "))
years = int(input("How many years? "))
balance = loanAmount
for i in range(years):
    balance += balance * .05
    print("Year ", years, "is", round(balance,2))

print("You paid", round(balance - loanAmount,2), "in interest!")
