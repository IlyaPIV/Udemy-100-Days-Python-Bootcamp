# with open("./weather-data.csv") as csv:
#     data = csv.readlines()
#
# print(data)

# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather-data.csv")
# print(data)
# print(type(data))
# print(data["temp"])
# print(type(data["temp"])
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)

print("\n======= AVERAGE =======\n")

avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)
# or
median_temp = data["temp"].mean()
print(median_temp)

print(f"\nmax temp = {data['temp'].max()}\n")

# Get data in Columns
print(data["condition"])
print(data.condition)

# Get data in Row
row_data = data[data.day == "Monday"]
print(row_data)
print(type(row_data))
max_temp_data = data[data.temp == data.temp.max()]
print(max_temp_data)

sunny_days = data[data.condition == 'Sunny']
print(sunny_days)
print(type(sunny_days))

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("new_data.csv")
