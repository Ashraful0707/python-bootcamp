# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
def two_digit_sub(two_digit_number):
    sum = 0
    while (two_digit_number != 0):
        sum = sum + (two_digit_number % 10)
        two_digit_number = two_digit_number//10
    return sum
print(two_digit_sub(int(two_digit_number)))
