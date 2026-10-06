# 
cars = ['audi','toyota','maruti']
print(cars.sort())
print("numbers of the item in the list:")
print(len(cars))
for car in cars :
    if car == 'toyota':
        print(f"\ni want to buy a {car.upper()}.")
    else:
        print(f"\ni want to buy a {car.title()}.") 
        
print("\nBut ferari is also a funtastic car.")
for car in cars[:2]:
    print(f"\n{car.title()}")

my_choice =  ['audi','toyota','maruti']
my_friend = my_choice[:]

print(f"my favorite cars are:")
print(my_choice)

print("\nmy friends choice are")
print(my_friend)

