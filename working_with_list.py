# Looping Through an Entire List

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
    
#for cat in cats:
#for dog in dogs:
#for item in item_lists:
# Donig More work within a for loop
# You can do just about anything with each item in a for loop. 
#Let's build on the previos example by printing a message to each magician,
# telling them that they performed a great trik.   
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"Hallo {magician.title()} you performed a great trik!")



#Let's add a second line to our message, telling each magician that we'er loking forword to their next trik:

    
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"Hallo {magician.title()} you performed a great trik!")
    print(f"i can't wait to see your next trik {magician.title()}.\n")
    
    
#Doing sonthing After a for loop 

magicians = ['alice','devid','carolina']
for magician in magicians:
    print(f"hallo {magician.title()} that waas the great trik")
    print(f"i can't wait to see your next trik{magician.title()}.\n")
    
print("Thank you ,everyone. That was the great magic show")
    
    
    
    
 
    
    
    
    
    
    
    
    