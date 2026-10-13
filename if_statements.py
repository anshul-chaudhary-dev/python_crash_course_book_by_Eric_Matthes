#If statements
# simple if statements

age = 19
if age >=18:
    print("you are old enough to vote")
    print("Have you registered to vote yet?")
    
    
#is-else statements
age = 17
if age>= 18:
    print("you are old enough to vote !")
    print("Have you registered to vote yet?")
    
else:
    print("sorry, you are too young to vote.")
    print("please registre to vote as soon as you turn 18!")
    
    
#if-elif-else:
    
age = 12 
if age <=4:
    print("Your admission cost is $0.")
elif age <= 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    
age = 68
if age <=4:
    price=0
elif age <= 18:
    price=25
elif age<65:
    price = 40
else:
    price=20
print(f"Your admission cost is ${price}")
    
    
# Omitting the else block 
age = 43
if age <=4:
    price=0
elif age <= 18:
    price=25
elif age<65:
    price = 40
elif age<=65:
    price=20
print(f"Your admission cost is ${price}")   
 

#test multiple conditions 

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("adding pepproni.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese.")
    
print("\nfinished making your pizza!.")





















    
    
    
    
    
    
    
    
    
    
    