# Matthew Roll
# Todays Date: June 16, 2025
# P1HW1
# This program calculates exponentiation and addition/subtraction based on user input

#Eponentition section
print("---Calculating Exponents---")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result_exp = base * exponent
print(base, "raised to the power of", exponent, "is", result_exp, "!!")

#Addition and Subtraction section is below
print("---Addition and Substraction---")
start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))
result_add_sub = (start_num + add_num) - sub_num
print(start_num, "+", add_num, "-", sub_num, "is equal to", result_add_sub)
