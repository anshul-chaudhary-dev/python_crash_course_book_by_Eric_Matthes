name = "anshul chaudhary"
print(name)
print(f"hallo,{name}")


#message for name hallo
name = "anshul chaudhary"
message = (name)
print(message)
print(f"Hallo,{message}")



#how to use f string?
first_name= "anshul"
last_name = "chaudhary"
message = (f"hallo how are {first_name} {last_name}".title())
print(message)

# how to use f string with title() method or upper() method
message = f"hallo how are you {'anshul chaudhary'}".upper()
print(message)

#comment=to add tab(\t) and newlines(\n) and add also title () method
print("python")
print('\tpython')
print("language:\n\tjavascript\n\tc\n\tpython".title())


#how to use r or l strip with f-string and changind strings with method 
name = " anshul chaudhary "
print(f"hallo how are you{name}".rstrip().title())
print(name.lstrip().upper())
print(name.strip().lower())


#multiple assignment:
x,y,z = 0,1,2
print(x)
print(y)
print(z)


#constants
constant = 'a constent is a variable whose value stays the same throughout the life of a progrsm.python doesnt have built-in contant types, but python prgrammers use all capital letters to indicate a variale should be treated as a constant and never be changed'
print(f"CONSTANT:\n\t{constant}".title())










