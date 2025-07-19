# Matt Roll
# 2025-07-10
# P4HW2 - Multi-Employee Salary Calculator
# This program calculates salary including overtime pay for multiple employees,
# collects data until the user enters "Done" for the employee name, and displays
# totals for overtime pay, regular pay, gross pay, and the number of employees entered.

# Pseudocode:
# 1. Initialize counters and accumulators for employees, overtime pay, regular pay, and gross pay.
# 2. Start a loop to collect employee data until "Done" is entered for employee name.
# 3. Prompt user for employee's name.
# 4. If name is "Done", exit the loop.
# 5. Prompt user for hours worked and pay rate.
# 6. Validate hours worked and pay rate (must be non-negative).
# 7. Calculate overtime hours (hours - 40 if hours > 40, else 0).
# 8. Calculate overtime pay (overtime hours * pay rate * 1.5).
# 9. Calculate regular pay (40 * pay rate if overtime, else hours * pay rate).
# 10. Calculate gross pay (regular pay + overtime pay).
# 11. Increment employee count and accumulate totals for overtime pay, regular pay, and gross pay.
# 12. Display individual employee details in a formatted table.
# 13. After loop ends, display totals for number of employees, overtime pay, regular pay, and gross pay.

# Initialize accumulators
employee_count = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    # Get employee name
    employee_name = input("Enter employee's name (or 'Done' to finish): ")
    
    # Check for sentinel value
    if employee_name.lower() == "done":
        break
    
    # Get hours worked and pay rate with validation
    while True:
        try:
            hours_worked = float(input("Enter number of hours worked: "))
            if hours_worked >= 0:
                break
            else:
                print("Hours worked cannot be negative. Please enter a valid number.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    
    while True:
        try:
            pay_rate = float(input("Enter employee's pay rate: "))
            if pay_rate >= 0:
                break
            else:
                print("Pay rate cannot be negative. Please enter a valid number.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    
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
    
    # Update accumulators
    employee_count += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    
    # Display individual employee results
    print("\nEmployee name:", employee_name)
    print(f"{'Hours Worked':<15} {'Pay Rate':<10} {'OverTime':<10} {'OverTime Pay':<15} {'RegHour Pay':<15} {'Gross Pay':<15}")
    print("-" * 80)
    print(f"{hours_worked:<15.1f} ${pay_rate:<9.2f} {overtime_hours:<10.1f} ${overtime_pay:<14.2f} ${regular_pay:<14.2f} ${gross_pay:<14.2f}")

# Display totals
print("\n" + "=" * 80)
print(f"{'Total Number of Employees Entered:':<40} {employee_count}")
print(f"{'Total Overtime Pay:':<40} ${total_overtime_pay:.2f}")
print(f"{'Total Regular Pay:':<40} ${total_regular_pay:.2f}")
print(f"{'Total Gross Pay:':<40} ${total_gross_pay:.2f}")
print("=" * 80)