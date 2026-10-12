#5.1 conditional test
car = 'subaru'
print("is car == 'subaru'? I pridict True")
print(car== 'subaru')

print("\nIs car == 'audi' ? I pridict False")
print(car == 'audi')


car = 'bmw'
print(car=='bmw')
print(car!='bmw')
print(car.upper())
print(car=='audi')
print(car!='audi')
print(car.lower()!='bmw')
print(car.upper()!='bmw')

#5.2 more condotional tests
car='bmw'
print(car=='bmw')
print(car!='audi')
print(car.lower()=='bmw')
print(car.lower()=='audi')
print(car.lower()!='audi')


players = 12
players_1 = 14
print(players==14)
print(players!=43)
print(players<14)
print(players>43)

print(players<=14) 
print(players>=43)
print((players<14)and(players_1>15))
print((players<14)or(players_1>15))

cars = ['toyota','maruti','bmw','audi']
for car in cars:
    if 'bmw' in car:
        print("bmw is my dream car")
        
        
        
cars = ['toyota','maruti','bmw','audi']
if 'byd' not in cars: 
    print("please try again after some days")
    
    


















