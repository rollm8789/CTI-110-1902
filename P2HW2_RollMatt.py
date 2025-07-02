
# Matt Roll
# 2025-06-23
# P2HW2 - Grade Summary
# This program prompts the user to enter grades for six modules, stores them in a list,
# and displays the lowest grade, highest grade, sum of grades, and average grade.

# Pseudocode:
# 1. Prompt the user to enter grades for six modules.
# 2. Store the grades in a list.
# 3. Calculate the lowest grade, highest grade, sum of grades, and average grade.
# 4. Display the results with appropriate formatting.

# Get user input for grades
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Calculate required values
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# Display results with formatting
print("\n-------------Results--------------")
print(f"{'Lowest Grade:'} {lowest_grade}")
print(f"{'Highest Grade:'} {highest_grade}")
print(f"{'Sum of Grades:'} {sum_of_grades}")
print(f"{'Average Grade:'} {average_grade:.2f}")
print("-------------------------------------")
