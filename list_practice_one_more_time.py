#list practice
# modifying
cars_list = ['honda','maruti','mg']
cars_list[0] = 'byd'
print(cars_list)

#Adding
#Appending = 1

cars_list = ['byd','maruti','mg']
cars_list.append('honda')
print(cars_list)


#appendin = 2

cars_list = []
cars_list.append('byd')
cars_list.append('maruti')
cars_list.append('mg')
cars_list.append('honda')
print(cars_list)


#inserting

cars_list = ['byd','maruti','mg']
cars_list.insert(1,'honda')
print(cars_list)

#removing
#del sattement

cars_list = ['byd','maruti','mg']
del cars_list[0]
print(cars_list)

#pop () method

cars_list = ['byd','maruti','mg']
cars = cars_list.pop(0)
print(f"i want to buy my dream car,{cars.title()}.")
print(cars_list)

#remove() method (when you know the value)

cars_list = ['byd','maruti','mg']
cars_list.remove('byd')
print(cars_list)


























