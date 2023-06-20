inp_line = input()
student_heights = inp_line.split(" ")

total_height = 0
for student in student_heights:
    total_height += int(student)

print(round(total_height / len(student_heights)))