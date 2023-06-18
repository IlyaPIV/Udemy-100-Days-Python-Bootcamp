# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round((weight / (height ** 2)), 1)

res = ""
if bmi < 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")


