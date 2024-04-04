# File not found

# with open("a_file.txt") as file:
#     file.read()
#           vs
try:
    file = open("a_file.txt")
    a_dictionary ={"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    print("There was an error opening file")
    file = open("a_file.txt", "w")
    file.write("New file was created")
except KeyError as error_message:
    print(f"The key {error_message} is not exist.")
else:
    print("Everything is ok")
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")


# Custom error throwing
height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Height is too high - should not be over 3 meters.")
bmi = weight / (height ** 2)
print(bmi)


# Exercise 1:
fruits = ["Apple", "Pear", "Orange", "Banana"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("There is no such fruit")
    else:
        print(fruit + " pie")


# Exercise 2:
facebook_posts = [
    {'Likes': 21, "Comments": 2},
    {'Likes': 13, "Comments": 2, 'Shares': 1},
    {'Likes': 15, "Comments": 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 1},
    {'Comments': 9, 'Shares': 2},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        print("This post doesn't have any likes")
        total_likes += 0
print("Total likes = ", total_likes)
