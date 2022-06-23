# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def pizza_order(size, add_pepperoni, extra_cheese):
    bill = 0

    small_pizza = 15        
    medium_pizza = 20
    large_pizza = 25

    pepperoni_for_small_pizza = 2
    pepperoni_for_medium_or_large_pizza = 3
    Extra_cheese_for_any_size_pizza = 1
    
    if (size == "S"):
        bill += small_pizza 
        if(add_pepperoni == "Y"):
            bill += pepperoni_for_small_pizza
    elif (size == "M"):
        bill += medium_pizza
        if(add_pepperoni == "Y"):
            bill += pepperoni_for_medium_or_large_pizza
    else:
        bill += large_pizza 
        if(add_pepperoni == "Y"):
            bill += pepperoni_for_medium_or_large_pizza
    if(extra_cheese == "Y"):
         bill += Extra_cheese_for_any_size_pizza
    return f'Your final bill is: ${bill}.'

print(pizza_order(size, add_pepperoni, extra_cheese))