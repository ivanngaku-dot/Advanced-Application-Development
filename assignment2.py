# Program Name: assignment2.py
# Course: IT3883/Section
# Student Name: Ivan Yann NGAKU FOSSO
# Assignment Number: Lab 2
# Due Date: 06/19/2026
# Purpose: The program calculate the students final average and then print then in descending order
# Resources:Textbook and PPIX files.

input_filename = "students_input.txt"

#list to store student data (name and average)
student_records = []

#Read the input file and process each line
input_file = open(input_filename, "r")

for each_line in input_file:

  cleaned_line = each_line.strip()

  if cleaned_line == "":
    continue 

  parts = cleaned_line.split()

  student_name = parts[0]

  score1 = float(parts[1])
  score2 = float(parts[2])
  score3 = float(parts[3])
  score4 = float(parts[4])
  score5 = float(parts[5])
  score6 = float(parts[6])
  
  total_scores = score1 + score2 + score3 + score4 + score5 + score6
  final_average = total_scores / 6
  
  student_records.append([student_name, final_average])

input_file.close()

sorted_students = sorted(student_records, key=lambda record: record[1], reverse=True)

for student in sorted_students:
    name = student[0]
    average = student[1]
    print(f"{name} {average:.2f}")