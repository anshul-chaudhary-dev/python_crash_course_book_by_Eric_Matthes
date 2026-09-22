# organize a list 
# Exercise practice

# 3.8 = seeing the world 
visit_place = ['moscow','japan','newzeeland','bhutan','europe']
print(visit_place)


# sorted () method
print(sorted(visit_place))

# orignal order
print(visit_place)


#sorted(reverse=TRUE)
visit_place = ['moscow','japan','newzeeland','bhutan','europe']
print(sorted(visit_place,reverse=True))


# orignal order
print(visit_place)

# reverse() method 
visit_place.reverse()
print(visit_place)

visit_place.reverse()
print(visit_place)


# sort() method
visit_place.sort()
print(visit_place)



# sort(reverse=True)
visit_place.sort(reverse=True)
print(visit_place)



# 3.9 = Dinner guest
guest = ['ujjawal','deepak','vaibhav','aakash','akhil']
print(guest)
print(len(guest))

# 3.10 = every functon:
    
location = ['moscow','japan','newzeeland','bhutan','europe']
print(location)
print(location[1].title())
print(location[-1].title())
print(location[2].title())
print(location)
location = ['moscow','japan','newzeeland','bhutan','europe']
print(location)
message = f"we want to go {location[1].title()} for study"
print(message)
location = ['moscow','japan','newzeeland','bhutan','europe']
print(location)
location[0] = 'thailand'
print(location)
location.append('moscow')
print(location)
location = []
location.append('moscow')
location.append('tokyo')
location.append('bhutan')
location.append('europe')
print(location)
location.insert(2,'taiwan')
print(location)
del location[2]
print(location)
no_visa = location.pop()
print(f"we dont have visa for {no_visa.title()}")
location.remove('tokyo')
print(location)
too_expensive = location[0]
location.remove(too_expensive)
print(f"\ntraveling for {too_expensive.title()} is too expensive")
print(location)

location = ['moscow','japan','newzeeland','bhutan','europe']
print(location)
location.sort()
print(location)
location.sort(reverse=True)
print(location)
print(sorted(location))
location.reverse()
print(location)
print(len(location))
print(location)
































