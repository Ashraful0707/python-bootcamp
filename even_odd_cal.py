# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def check_even_odd(number):
    if (number % 2) == 0:
        return "This is an even number"
    else: 
        return "This is an odd number"
print(check_even_odd(number))