# About
# Name: Matthew Roll
# Date: 7-7-2025
# Homework: P4LAB2 - Multiplication Table
# Description: This program prompts the user for an integer and displays its multiplication
#              table from 1 to 12 using a for loop if the integer is zero or positive.
#              If the integer is negative, it displays an error message. A while loop
#              controls whether the program runs again based on user input ("yes" or "no").

# Main program
while True:
    # Get user input
    try:
        num = int(input("Enter an integer: "))

        # Check if number is negative
        if num < 0:
            print("Cannot accept negative values.")
        else:
            # Display multiplication table using for loop
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")

        # Ask if user wants to run again
        again = input("Do you wish to run the program again? (yes/no): ").lower()

        # Check user response
        if again != "yes":
            break
    except ValueError:
        print("Please enter a valid integer.")
