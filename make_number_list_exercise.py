
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
  

squares = [value**2 for value in range(1,11)]
print(squares)

# 4.3: Counting to twenty: Use a for loop to print the number  from 1 to 20, inclusive

for num in range(1, 21):
    print(num)
    
# 4.4 : one million : make a list of the numbers from one to one million and then use a for loop to print the numbers.
#if output is taking too long stop it by pressing CTRL or by closing the output window.

#numbers = list(range(1, 1000001))
# 4.5: SUmming a million:
     
    
#print(numbers) 
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))


# 4.6 Odd numbers :

numbers = []
for odd_numbers in range(1,21,2):
     numbers.append(odd_numbers)
print(numbers)


#4.7 threes:

numbers = list(range(3,31,3))
for num in numbers:
    print(num)


# exercise 4.8. Cubes:
# 4.9


cubes = [value**3 for value in  range(1,11)]
for cube in cubes:
    print(cube)






    


    