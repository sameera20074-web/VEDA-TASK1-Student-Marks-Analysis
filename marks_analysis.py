# Student Marks Analysis - Task 1
# VEDA Technology - AI & ML Track

student_marks = [85, 92, 78, 90, 65, 88, 72, 95, 60, 82]

total_marks = sum(student_marks)
highest_marks = max(student_marks)
lowest_marks = min(student_marks)
average_marks = total_marks / len(student_marks)

print("----- Student Marks Analysis -----")
print(f"Marks List: {student_marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
