# variable = a container for value(string, integer, float, boolean, etc)
# a variable behaves as if it was the value it contains

#Strings
first_name = "Ssara"
food = "dahi k aaloo"
email = "fake@fake.com"
print(first_name)
print(f"Hello {first_name}")
print(f"{first_name} You like {food}")
print(f"{first_name} Your email is {email}")

#integers
age = 22
quantity = 3
num = 44
print (f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"There are {num} students in class")

#float
price = 90.89
cgpa = 8.54
distance = 9.1

print(f"the price is {price}")
print(f"{first_name} Your CGPA is {cgpa}")
print(f"The distance is {distance} km")

#Boolean
is_student = True
if is_student:
    print("You are a student")
else:
    print("You are not a student")

for_sale = False
if for_sale:
    print("Is for sale")
else:
    print("Is not for sale")
