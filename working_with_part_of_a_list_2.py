# tuples :
# difiining a tuple : 
# A Tuple looks just like a list ,expect you use parentheses instead of square brackets .
# Once you define a tuple,you can axess individual elements by using each item's index, justas you would for a list.
# For example : if we have a rectangle that should always be a certain size we canensure that its size doesnt change by putting the dimensions into a tuple :

    
dimensions = (200, 50 )
print(dimensions[0])
print(dimensions[1])


# Looping through all values in a Tuple : 
    
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
    
    
# Writing over a tuple : 
 
dimensions = (200, 50 )
print("original dimensions")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400,200)
print("\nmodified dimensions:")
for dimension in dimensions:
    print(dimension)
    
    
# exercise 4.13:

offers = ('bergur','pizza','idli','dosa')
print('Offer foods:')
for offer in offers:
    print(offer)
offers = ('bergur','idli')
print('\nānew foods offer:')
for offer in offers:
    print(offer)
    
    
    
    
    
    
    
    
    
    
    
    
    