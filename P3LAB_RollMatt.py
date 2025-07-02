
# P3LAB_LastnameFirstname
# Author: Your Lastname Your Firstname
# Date: June 30, 2025
# Description: This program calculates the most efficient combination of dollars, quarters, dimes, nickels, and pennies
# to make a given amount of money entered by the user as a float with two decimal places.


money = float(input("Enter an amount of money as a float: $"))

cents = int(round(money * 100)) # Use round to avoid floating-point issues

dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

# Print header
print("You need:")

# Print each denomination on its own line, no extra spaces
if dollars > 0:
 print(f"{dollars} {'dollar' if dollars == 1 else 'dollars'}")
if quarters > 0:
 print(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")
if dimes > 0:
 print(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")
if nickels > 0:
 print(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")
if pennies > 0:
 print(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")

# Handle case where no denominations are needed
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
 print("No Change")
