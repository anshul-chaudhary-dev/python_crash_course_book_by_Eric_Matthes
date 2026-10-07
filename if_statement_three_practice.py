# 1. A simple example 

cars =['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
        
# coditional tests:
# checking for Equality:
    
car = 'bmw'
if car =='bmw':
    print(car.upper())


car = 'audi'
if car == 'bmw':
    print(car)
# this is false so code is not run here


# Ignoring Case When Checking For Equality == :
    
car = 'AUDI'
if car.lower() == 'audi':
   print(car)
   

# Checking For Ineuality  !=  :
    
requested_topping = 'mushrooms'
if requested_topping !='anchovies':
    print('Hold the anchovies')
    
    
# Numerical Comperissions :
    
answer = 17
if answer != 42:
    print("that is not the correct answeer, please try again ")
    





















    