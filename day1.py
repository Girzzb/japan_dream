print("My dream is to be a Software Engineer in Japan!")
name = input("What's your name? ")
print(f"Hello {name}, let's code to make it happen!")

name = "adomx" # str
age = 16 # int
height = 1.75 # float
is_coder = True # bool

# Condition
print(f"{name} is {age} years old, {height}cm tall, coder? {is_coder}")
age = int(input("How old are you? "))
if age >= 18:
    print("You're an adult!")
elif age >= 16:
    print("You're ready to code!")
else:
    print("You're young, keep learning!")

# For loop
print("Counting to Japan:")
for i in range(1, 6):
    print(f"Year {i}")

# While loop
count = 0
while count < 3:
    print("Code every day!")
    count = count + 1

# Exercise 1: Calculate BMI
weight = float(input("Weight (kg): "))
height_cm = float(input("Height (cm): "))
height_m = height_cm / 100 # Convert cm to m
bmi = weight / (height_m * height_m)
if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
