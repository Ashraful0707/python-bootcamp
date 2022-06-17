
two_digit_number = input("Type a two digit number: ")

def two_digit_sub(two_digit_number):
    return 0 if two_digit_number == 0 else int(two_digit_number % 10) + two_digit_sub(int(two_digit_number / 10))