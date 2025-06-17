# Pseudocode:
# 1. Start
# 2. Ask the user to enter their total travel budget
# 3. Ask the user to enter their travel destination
# 4. Ask the user how much they expect to spend on gas
# 5. Ask the user how much they expect to spend on accommodation/hotel
# 6. Ask the user how much they expect to spend on food
# 7. Calculate the total expenses by adding gas, accommodation, and food
# 8. Subtract the total expenses from the budget to get the remaining balance
# 9. Display the travel destination, initial budget, individual expenses, and remaining balance
# 10. End

# Matthew Roll
# June 16, 2025
# P1HW2 - Travel Expenses
# This program calculates and displays travel expenses based on user input

# User inputs
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

# Calculate total expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results

print("-----------Travel Expenses----------")
print("Location:", destination)
print("Initial Budget:", budget)
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print("Remaining Balance:", remaining_balance)
