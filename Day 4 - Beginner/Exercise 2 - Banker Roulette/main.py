# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ppl_count = len(names)
person = random.randint(0, ppl_count-1)
print(f"{names[person]} is going to buy the meal today!")
