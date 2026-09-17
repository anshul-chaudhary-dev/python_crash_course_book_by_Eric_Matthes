#Exercise
#3.4 = Guest List:
# If you could invite any one, living or deceased, to dinner, who you invite . 
# Make a list that includes at least three people you'd lilke to invite to dinner.
#then use your list to print a message to each person , inviting them to dinner.

guest = ['vaibhav', 'vasu','deepak']
print(guest)
print(f"Hallo {guest[0].title()} you are inviting for Dinner")
print(f"Hallo {guest[1].title()} you are inviting for Dinner")
print(f"Hallo {guest[-1].title()} you are inviting for Dinner")


# 3.5 Changing Guest List
#start with your programme from exercise 3.4.
#Add a print() call at the end of your programme, stating the name of the guest who cant make it.
print(f"{guest[0]} cannot make it  unfortunately")

guest[0] = "shailesh"
print(guest)
print(f"Hallo {guest[0].title()} you are inviting for Dinner")
print(f"Hallo {guest[1].title()} you are inviting for Dinner")
print(f"Hallo {guest[-1].title()} you are inviting for Dinner")


# 3.6 More Guest


guest.insert(0, "vaibhav")
guest.insert(2,"akhil")
guest.insert(-2, "chotu")
print(guest)
print(f"Hallo {guest[0].title()} you are inviting for Dinner")
print(f"Hallo {guest[1].title()} you are inviting for Dinner")
print(f"Hallo {guest[2].title()} you are inviting for Dinner")
print(f"Hallo {guest[3].title()} you are inviting for Dinner")
print(f"Hallo {guest[4].title()} you are inviting for Dinner")
print(f"Hallo {guest[-1].title()} you are inviting for Dinner")

#3.7 Shrinking guest
print(f"we can invite only 2 people for dinner")
print(guest)
uninvited_guest = guest.pop(1)
print(f"hallo {uninvited_guest} onfortunately we have to uninviteed you")
uninvited_guest = guest.pop(2)
print(f"hallo {uninvited_guest} onfortunately we have to uninviteed you")
print(uninvited_guest)
print(guest)
uninvited_guest = guest.pop(1)
print(f"hallo {uninvited_guest} onfortunately we have to uninviteed you")
uninvited_guest = guest.pop(-2)
print(f"hallo {uninvited_guest} onfortunately we have to uninviteed you")
print(guest)
print(f"Hallo {guest[0].title()} you are inviting for Dinner")
print(f"Hallo {guest[1].title()} you are inviting for Dinner")

del guest[0]
print(guest)
del guest[0]
print(guest)




