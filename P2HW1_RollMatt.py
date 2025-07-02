
# Matt Roll
# 2025-06-23
# P2HW1 - Travel Budget Summary
# This program prompts the user for travel destination, budget, and expenses (fuel, accommodation, food),
# then displays a formatted summary including total expenses and remaining budget.

# Get user input
destination = input("Enter your travel destination: ")
budget = float(input("Enter your initial budget: "))
fuel_cost = float(input("Enter fuel cost: "))
accommodation_cost = float(input("Enter accommodation cost: "))
food_cost = float(input("Enter food cost: "))

# Calculate total expenses and remaining budget
total_expenses = fuel_cost + accommodation_cost + food_cost
remaining_budget = budget - total_expenses

# Display results with formatted output
print("\n------------Travel Expenses-----------")
print(f"{'Destination:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel Cost:':<20} ${fuel_cost:.2f}")
print(f"{'Accommodation Cost:':<20} ${accommodation_cost:.2f}")
print(f"{'Food Cost:':<20} ${food_cost:.2f}")
print(f"{'Total Expenses:':<20} ${total_expenses:.2f}")

print("-----------------------------------------")

print(f"{'Remaining Budget:':<20} ${remaining_budget:.2f}")