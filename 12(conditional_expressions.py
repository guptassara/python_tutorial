num = float(input("Enter a number: "))

print("positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

num2 = float(input("Enter another number: "))
print(f"Max number is: {num}" if num > num2 else f"Max number is: {num2}")
print(f"Min number is: {num}" if num < num2 else f"Min number is: {num2}")

age = int(input("Enter your age: "))
status = "Adult" if age>=18 else "Child"
print(f"You are {status}")

