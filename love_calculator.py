# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def love_calculator(name1, name2):
    word1 = "TRUE"
    word2 = "LOVE"
    word1_lowercase = word1.lower()
    word2_lowercase = word2.lower()
    count1 = 0
    count2 = 0
    combined_name = (name1 + name2).lower()
    for letter in combined_name:
        if letter in word1_lowercase:
            count1 += 1
        if letter in word2_lowercase:
            count2 += 1
    total_love_score = int(str(count1) + str(count2))
    
    if (total_love_score<10 or total_love_score>90):
        return f'Your score is {total_love_score}, you go together like coke and mentos.'
    elif (total_love_score>40 and total_love_score<50):
        return f'Your score is {total_love_score}, you are alright together.'
    else:
        return f'Your score is {total_love_score}.'

print(love_calculator(name1, name2))

