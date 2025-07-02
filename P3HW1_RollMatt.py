# Matt Roll
# 2025-07-01
# P3HW1 - Grade Summary
# This program prompts the user to enter grades for six modules, stores them in a list,
# and displays the lowest grade, highest grade, sum of grades, and average grade.
# Pseudocode:
# 1. Prompt the user to enter grades for six modules.
# 2. Store the grades in a list.
# 3. Calculate the lowest grade, highest grade, sum of grades, and average grade.
# 4. Display the results with appropriate formatting.
# Get user input for grades
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
# Add grades to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# Fixed: Corrected syntax (commas, variable names)
# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)
# Display results with formatting
print("\n-------------Results--------------")
print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total}")
print(f"Average Grade: {avg:.2f}")
print("-------------------------------------")
# Determine letter grade for average
if avg >= 90:
print('Your grade is: A')
elif avg >= 80:
print('Your grade is: B')
elif avg >= 70:
print('Your grade is: C')
elif avg >= 60:
print('Your grade is: D')
else:
print('Your grade is: F')