val1 = []
with open("file1.txt") as file1:
    lines = file1.readlines()
    for line in lines:
        val1.append(int(line.strip()))

val2 = []
with open("file2.txt") as file2:
    lines = file2.readlines()
    for line in lines:
        val2.append(int(line.strip()))


result = [val for val in val1 if val2.__contains__(val)]

# Write your code above 👆
print(result)




student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# Loop for rows in DF
for (index, row) in student_data_frame.iterrows():
    print(f"#{index}:")
    print(row.student + " - " + str(row.score))
