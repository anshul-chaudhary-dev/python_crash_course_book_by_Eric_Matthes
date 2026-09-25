#Using the range() Function:

for value in range(1, 5):
    print(value)
    
# Using range () to make a list of Numbers

even_numbers = list(range(2,11,2))
print(even_numbers)

# that is the square of each integer from 1 through 10:

squares = []
for value in range(1, 11):
    square = value **2
    squares.append (square)
print(squares)


#To write code more concisel ,omit the temprery vriable square and append each new value directly to the list:

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# you can easily find minimum, maximum, and sum of a list of numbers:

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))




























