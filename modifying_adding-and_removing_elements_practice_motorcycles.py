# Modifying elements in a list:
motorcycles = ['honda','ymaha','suzuki']
print(motorcycles)
motorcycles[0] = "dugati"
print(motorcycles)
motorcycles[-1] = "triump"
print(motorcycles)


# Adding elements to a list:
#you imght want to add a new element to a list for many reasons.
# for example, you might want to make a new aliens appear in a game
#or add new data to a visualization.
#or new register users to a websites you've buit.
#Python provides several ways to add new data to existing list.

#Appending Elements to the end of a list:
# the simplest way to add a new element to a list is to append the item to the list.
#Whenyou append an item to a list, the element is added to the end of the list.
# For Example:

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append("dugati")
print(motorcycles)
#here the append() method adds 'dugati' to the end of the list, without affecting any of the other elements in the list.


# Using an empty list[] lets add the elements 'homda', 'yamaha', 'suzuki'

motorcycles = []
print([])

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


#Insert elements into a List:
# You can add a new element at any position in you rlist by using insert() method'
#For example:
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(-2,"dugati")
print(motorcycles)

#one more example
cars_names = ['suzuki', 'toyota','byd','mahindra']
cars_names.insert(2,"mg")
print(cars_names)



#Rmoving element from list:
#Often you'll want to remove an item or a set of items from a list.
# For example, when a player shoots down an alien from the sky, you'll most likely want to remove it from the list of active aliens.
# Or when a user decide to cancel their account on a web aplication you created,you'll want to remove that user from the list of avtive users.
# You can remove an item according to its position in the list or according to its value.


# Removing an Item using the del statement:
    
motorcycles = ['honda','yamaha','suzuki','dugati']
print(motorcycles)
del motorcycles[-2]
print(motorcycles)

#Here we use the del statement to remove the 3rd item (-2),'suzuki' from the list of motorcycles
  


# Removing an item using the po() method
# . sometimes you'll want to use the value of an item afer you remove it from a list 
# . The pop90 method remove the last item you work with that item after removing it.
# For Example 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop(-1)
print(motorcycles)
print(popped_motorcycles)

# The ouput show that the value 'suzuki' was removed from the end of the list and is now assigned to the variable popped_motorcycles.


# We can use the pop() method to print a statement about the last motocycle, we bought.

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop(2)
print(f"The last motorcycle I owned was a {last_owned.title()}")

# The output is a simple sentence about the most recent motorcycle we owned.


# Removing an item by value 
# sometimes you wont know the position of the value you want to remove from the list.
# If you only know the value of the item you want to remove , you can use the remove() method.
#For example:
motorcycles = ['honda', 'yamah','suzuki','dugati']
print(motorcycles)
motorcycles.remove('dugati')
print(motorcycles)

# here the remove() method tells python to figure out where 'dugati' appear in the list of motorcycles.


# Lets remove the value 'dugati' and print ression for removing it from the list:

motorcycles = ['honda','yamaha','suzuki','dugati']
print(motorcycles)
too_expensive = "dugati"
print(too_expensive)
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} too expensive for me")





