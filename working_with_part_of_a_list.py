# Working with part of the list 
# Slicing a list 

players = ['charles', 'martina','micheal','florence','eli']
print(players[0:3])

print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])


# Looping though a slice 
 
players = ['charles', 'martina','micheal','florence','eli']
print("here are the first three players on my team")
for player in players[:3]:
    print(player.title())
    
    
#example 1 =

scores = [98,95 ,90,85,80,72]
print("top three scores")
for score in scores[:3]:
     print(score)
     
# example 2= skip the first eliment 

members = ['alice','bob','charie','david']
for member in members[1:]:
    print(member)
    
    
# example 3 middle element 

nums = [10,20,30,40,50,60,]
print("middle numbers")
for num in nums[1:-1]:
    print(num)
    
# Copying list 

my_foods = ['pizza','falafel','carrat cake']
friend_foods = my_foods[:]

print("my favorite foods are")
print(my_foods)
print("\nmy friends favorite foods are ")
print(friend_foods)

my_foods.append('burger')
friend_foods.append('icecream')
print(my_foods)
print(friend_foods)
























