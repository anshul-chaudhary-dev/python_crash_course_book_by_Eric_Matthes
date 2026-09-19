bicycles = ['trek','cnnondale','redline','specialized']
print(bicycles)


#accesing element in a list
bicycles = ['trek','cnnondale','redline','specialize']
print(bicycles[0])
print(bicycles[0].title())

#Index position satrt at 0 not 1 
print(bicycles[1])
print(bicycles[-1])


#using individual value
message = f"my first bicycle was a {bicycles[0].title()}"
print(message)

#exercise:

friend_name = ['vaibhav','deepak','vasu','ujjawal']
print(friend_name[0].title())
print(friend_name[1].title())
print(friend_name[2].title())
print(friend_name[3].title())


friend_name = ['vaibhav','deepak','vasu','ujjawal']
print(f"hallo {friend_name[0]} how are you today")
print(f"hallo {friend_name[1]} how are you today")
print(f"hallo {friend_name[2]} how are you today")
print(f"hallo {friend_name[3]} how are you today")


car = ['maruti','honda','mg','bmw']
print(f"Iwould like to own a {car[0].title()} car")
print(f"Iwould like to own a {car[1].title()} car")
print(f"Iwould like to own a {car[2].title()} car")
print(f"Iwould like to own a {car[-1].title()} car")



#modifying,adding and removing elements
#modifying element in a list

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#modifying
motorcycles[2]='dugati'
print(motorcycles)


#adding element to list
# Appending elements to the end of the list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#appending
motorcycles.append('dugati')
print(motorcycles)


motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('dugati')
print(motorcycles)





#Insert Elements into a list
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(3,'dugati')
print(motorcycles)


#removing elements from a list

#removing an item using the del statements

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
# If you know the position of the item you want to remove from a list.
# You can use del statements
del motorcycles[1]
print(motorcycles)


# Removing an item using the pop() method
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#pop() method
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop(1)
print(f"the last mototcycle i owned was a {last_owned.title()}.")


#Removing an item by value
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#remove() method
motorcycles.remove('honda')
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me ")


# Exercise 3.4 guest_list:

guest_list = ['vaibhav','deepak','ujjawal']
print(f"Hllo, {guest_list[0].title()} i would like to invite you for dinner")
print(f"Hllo, {guest_list[1].title()} i would like to invite you for dinner")
print(f"Hllo, {guest_list[-1].title()} i would like to invite you for dinner")

guest_list = ['vaibhav','deepak','ujjawal']
print(f"sorry, {guest_list[2].title()} you cant make the dinner")
guest_list[2] = 'shailesh'
print(guest_list)
print(f"Hllo, {guest_list[0].title()} i would like to invite you for dinner")
print(f"Hllo, {guest_list[1].title()} i would like to invite you for dinner")
print(f"Hllo, {guest_list[-1].title()} i would like to invite you for dinner")




guest_list = ['vaibhav','deepak','ujjawal']
print(f"Hallo everyone i just want to inform you, i found a big table for dinner")
guest_list.insert(0,'shailesh')
guest_list.insert(2,'akhil')
guest_list.insert(5,'vasu')
print(guest_list)
print(f"Hllo, {guest_list[0].title()} i would like to invite you for dinner")
print(f"Hllo, {guest_list[1].title()} i would like to invite you for dinner")
print(f"Hllo, {guest_list[2].title()} i would like to invite you for dinner")
print(f"Hllo, {guest_list[3].title()} i would like to invite you for dinner")
print(f"Hllo, {guest_list[4].title()} i would like to invite you for dinner")
print(f"Hllo, {guest_list[5].title()} i would like to invite you for dinner")

print(f"sorry, everyone but today i can invite only two people for dinner")


uninvited_guest = guest_list.pop(0)
print(f"sorry for that but {uninvited_guest.title()} you are not invited today")
uninvited_guest = guest_list.pop(0)
print(f"sorry for that but {uninvited_guest.title()} you are not invited today")
uninvited_guest = guest_list.pop(1)
print(f"sorry for that but {uninvited_guest.title()} you are not invited today")
uninvited_guest = guest_list.pop(-1)
print(f"sorry for that but {uninvited_guest.title()} you are not invited today")
print(guest_list)
print(f"Hallo,{guest_list[0].title()} i would like to invite you for dinner")
print(f"Hallo,{guest_list[1].title()} i would like to invite you for dinner")

del guest_list[0]
del guest_list[0]
print(guest_list)












































































