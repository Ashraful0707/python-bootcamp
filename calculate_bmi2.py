# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
def bmi(height, weight):
    BMI = round(weight/(height**2))
    # return BMI
    if BMI < 18:
        return f"Your BMI is {BMI}, you are underweight."
    elif BMI < 25:
        return f"Your BMI is {BMI}, you have a normal weight."
    elif BMI < 30:
        return f"Your BMI is {BMI}, you are slightly overweight."
    elif BMI < 35:
        return f"Your BMI is {BMI}, you are obese."
    else:
        return f"Your BMI is {BMI}, you are clinically obese."

print(bmi(height,weight))