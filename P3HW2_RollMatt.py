# Matthew Roll
# July 01, 2025
# P3HW2
# A program to calculate employee salary including overtime pay

# Pseudocode:
# 1. Prompt user to enter employee's name and store it
# 2. Prompt user to enter number of hours worked and store it
# 3. Prompt user to enter employee's pay rate and store it
# 4. Check if hours worked exceed 40 to determine overtime
# 5. If overtime exists, calculate overtime hours (hours - 40)
# 6. Calculate overtime pay (overtime hours * pay rate * 1.5)
# 7. Calculate regular pay (40 * pay rate if overtime, else hours * pay rate)
# 8. Calculate gross pay (regular pay + overtime pay)
# 9. Display employee name, hours worked, pay rate, overtime hours, overtime pay, regular pay, and gross pay

# Get input from user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate overtime and pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("\nEmployee name:", employee_name)
print("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay", sep="\t\t")
print("-" * 60)
print(f"{hours_worked:>12.1f}\t\t{pay_rate:>8.1f}\t\t{overtime_hours:>8.1f}\t\t{overtime_pay:>12.2f}\t\t{regular_pay:>12.2f}\t\t{gross_pay:>12.2f}")