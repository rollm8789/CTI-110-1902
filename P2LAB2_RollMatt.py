
# Matthew Roll
# 2025-06-23
# P2LAB2 - Vehicle MPG Calculator
# This program creates a dictionary with vehicle names as keys and their MPG as values.
# It then prompts the user to select a vehicle, enter the miles to drive, and calculates the gallons of gas needed.

# Create the dictionary
vehicle_mpg = {
 "Camaro": 18.21,
 "Prius": 52.36,
 "Model S": 110,
 "Silverado": 26
}

# Get all the keys in the dictionary
keys = vehicle_mpg.keys()

# Print the keys
print("Available vehicles:")
print(keys)

# Prompt the user to enter a vehicle
vehicle = input("Enter the vehicle name: ")

# Display the MPG for the selected vehicle
mpg = vehicle_mpg[vehicle]
print(f"The MPG for {vehicle} is {mpg}.")

# Prompt the user to enter the number of miles
miles = float(input("Enter the number of miles you will drive: "))

# Calculate the gallons of gas needed
gallons_needed = miles / mpg

# Display the gallons of gas needed, rounded to two decimal places
print(f"Gallons of gas needed: {gallons_needed:.2f}")

# Save the code to a file
with open('P2LAB2_LastnameFirstname.py', 'w') as f:
 f.write("""# Your Name
# 2025-06-23
# P2LAB2 - Vehicle MPG Calculator
# This program creates a dictionary with vehicle names as keys and their MPG as values.
# It then prompts the user to select a vehicle, enter the miles to drive, and calculates the gallons of gas needed.

# Create the dictionary
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all the keys in the dictionary
keys = vehicle_mpg.keys()

# Print the keys
print("Available vehicles:")
print(keys)

# Prompt the user to enter a vehicle
vehicle = input("Enter the vehicle name: ")

# Display the MPG for the selected vehicle
mpg = vehicle_mpg[vehicle]
print(f"The MPG for {vehicle} is {mpg}.")

# Prompt the user to enter the number of miles
miles = float(input("Enter the number of miles you will drive: "))

# Calculate the gallons of gas needed
gallons_needed = miles / mpg

# Display the gallons of gas needed, rounded to two decimal places
print(f"Gallons of gas needed: {gallons_needed:.2f}")
""")

print("The code has been saved to P2LAB2_LastnameFirstname.py")

