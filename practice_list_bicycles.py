#in python. square brakets ([]) indicate a list,and individual elements in the list are seprated by commas.
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
#this is not the output you want your users to see.


#accessing eliment in a list.
bicycles = ['terk','cannondale','redline','specialized']
print(bicycles[0])
#this the result you want to your user to see.


#index position starts at 0, not 1
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-3])




#using the individual value from a list and composing a message
bicycles = ['trek','cannondale','redline','specialized']
message = f"my first bicycle was a {bicycles[0].title()}"
print(message)


#exercise 3.1
name = ['vaibhav','deepak','ujjawal','shailesh']
print(name[0].title())
print(name[1].title())
print(name[2].title())
print(name[-1].title())

#exercise 3.2
name = ['vaibhav','deepak','ujjawal','shailesh']
print(f"hallo,{name[0].title()} are you free to meet in the evening")
print(f"hallo,{name[1].title()} are you free to meet in the evening")
print(f"hallo,{name[2].title()} are you free to meet in the evening")
print(f"hallo,{name[-1].title()} are you free to meet in the evening")


#exercise 3.3
cars_name = ['maruti','honda','mg','mahindra','toyota']
print(f"I would like to own a {cars_name[0].title()} car.")
print(f"I would like to own a {cars_name[1].title()} car.")
print(f"I would like to own a {cars_name[2].title()} car.")
print(f"I would like to own a {cars_name[-1].title()} car.")



#another exercise from my side
cars_name = ['maruti','honda','mg','mahindra','toyota']
print("cars_name:\nmaruti\nhonda\nmg\nmahindra\n\ttoyota")
