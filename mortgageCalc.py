import math

#Receive user input
rate = input("What is the yearly interest rate on the loan? ")
years = input("Number of years for loan? ")
amount = input("Loan amount? ")

#Perform loan calculations
mnthlyInterest = rate / 1200
mnthlyPayment = amount * mnthlyInterest/(1 - (pow(1 / ( 1 + mnthlyInterest), years * 12)))
total = mnthlyPayment * (years * 12)

#Result to the program
print("Your monthly payment will be: " + str(mnthlyPayment))
print("Your total payment amounts will be: " + str(total))