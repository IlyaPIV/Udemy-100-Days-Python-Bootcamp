# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_weight = int(weight)
float_height = float(height)
bmi = int_weight / float_height ** 2
# print(str(int_weight) + " ÷ (" + str(float_height) + " x " + str(float_height) + ") = " + str(bmi))
print(int(bmi))