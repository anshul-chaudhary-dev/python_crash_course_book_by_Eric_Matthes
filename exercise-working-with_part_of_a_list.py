# 4.10 slices:
    
animals = ['dog','cat','goat','cow']
print("the first three animals in the list are")
for animal in animals[:3]:
    print(animal.title())
    
animals = ['dog','cat','goat','horse','cow']
print("three animals from the middle of the list are")
for animals in animals[2:5]:
    print(animals.title())
    
    
animals = ['dog','cat','goat','horse','cow']
print("the last three items in hte list are :")
for animal in animals[2:]:
    print(animal.title())
    
    
 # 4.11=
 
my_pizzas = ['paneer mkahani','peppy paneer','indi chiken tikka','veg ectrvaganza','farmhouse']
friend_pizzas = my_pizzas[:]
print(my_pizzas)
print(friend_pizzas)
my_pizzas.append('cheese n corn')
friend_pizzas.append('loaded')
print(my_pizzas)
print(friend_pizzas)

print("my favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)
    
print("\nmy friends favorite pizza are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
    

    

























 
 