# USING range() to make a list of numbers:
    
numbers = list(range(1, 6))
print(numbers)


# even numbers using list() function and range() function:

even_numbers = list(range(2,11,2))
print(even_numbers)



# That the square to each interger from 1 through 10:

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(min(squares))
print(max(squares))
print(sum(squares))

#list comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)