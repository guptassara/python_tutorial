age = int(input("Enter your age: "))
if age>=100:
    print("You are too old to sign up")
elif age>=18 :
    print("You are now signed up")
elif age<0:
    print("You haven't been born yet!!")
else:
    print("You must be 18+ to sign up")
    
response = str(input("Would you like some food? Y/N? "))
if response == 'Y':
    print("You can have food")
elif response == 'N':
    print("No food for you!!!")
    
for_sale = True
if for_sale:
    print("For sale")
else:
    print("Not for sale")