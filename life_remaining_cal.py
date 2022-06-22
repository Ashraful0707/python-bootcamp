# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def life_time_remaining(age):
    years_left = 90 - int(age)
    month_left = years_left * 12
    weeks_left = years_left * 52
    days_left = years_left * 365
    msg = f"You have {days_left} days, {weeks_left} weeks, and {month_left} months left"
    return msg

print(life_time_remaining(age))