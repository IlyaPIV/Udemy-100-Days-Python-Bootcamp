import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
fur_colors = ["Gray", "Black", "Cinnamon"]
squirrels_count = []
for color in fur_colors:
    squirrels = data[data["Primary Fur Color"] == color]
    count = len(squirrels)
    squirrels_count.append(count)
print(squirrels_count)

squirrels_data = {
    "colors": fur_colors,
    "count": squirrels_count
}
data_frame = pandas.DataFrame(squirrels_data)
print(data_frame)
data_frame.to_csv("squirrels_count.csv")
