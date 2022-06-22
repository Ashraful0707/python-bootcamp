# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def bmi(height, weight):
    BMI = weight/(height**2) 
    return BMI
print(round(bmi(float(height), int(weight))))