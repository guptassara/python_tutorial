name = input("Enter your name: ")
if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")

print("From while loop")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name again: ")

print(f"Hello {name}!!")


age = int(input("Enter your age: "))
while age < 0:
    print("Age can not be egative")
    age = int(input("Enter age: "))

print(f"Hello {name}! You are {age} years old")


food = input("Enter food you like(press q to quit): ")

while not food == "q":
    print(f"{name} You like {food}")
    food = input("Your another favorite food is (q to quit): ")
print("Byeee!!!")

num = int(input("Enter number bewteen 1 to 10 "))
while num < 1 or num > 10:
    print(f"{num} is invalid")
    num = int(input("Enter number between 1 to 10 "))
print(f"You entered {num}")
