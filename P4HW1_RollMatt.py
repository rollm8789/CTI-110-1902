# Matt Roll
# 2025-07-10
# P4HW1 - Enhanced Grade Summary
# This program prompts the user to enter the number of scores they want to input,
# collects valid scores (0-100) using a loop, stores them in a list, drops the lowest score,
# calculates the average of the remaining scores, determines the letter grade,
# and displays the results.

# Pseudocode:
# 1. Prompt user for the number of scores to enter.
# 2. Initialize an empty list to store scores.
# 3. Use a loop to collect the specified number of scores:
#    a. Prompt user for a score.
#    b. Validate the score (0-100) using a while loop.
#    c. If invalid, notify user and request a valid score.
#    d. If valid, append to the scores list.
# 4. Calculate the lowest score.
# 5. Create a modified list by removing the lowest score.
# 6. Calculate the average of the modified list.
# 7. Determine the letter grade based on the average:
#    - A: 90-100
#    - B: 80-89
#    - C: 70-79
#    - D: 60-69
#    - F: Below 60
# 8. Display results: lowest score, modified list, average, and letter grade.

# Get number of scores from user
num_scores = int(input("Enter the number of scores you would like to enter: "))

# Initialize empty list for scores
scores = []

# Loop to collect scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Calculate required values
lowest_score = min(scores)
modified_scores = scores.copy()
modified_scores.remove(lowest_score)
average_score = sum(modified_scores) / len(modified_scores) if modified_scores else 0

# Determine letter grade
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display results
print("\n--------------Results--------------")
print(f"{'Lowest Score:':<20} {lowest_score:.2f}")
print(f"{'Modified List:':<20} {modified_scores}")
print(f"{'Scores Average:':<20} {average_score:.2f}")
print(f"{'Letter Grade:':<20} {letter_grade}")
print("-----------------------------------")