weight = float(input("Enter your weight "))
unit = input("is this weight in Kilo grams or pound? k/p ")
if unit == 'k':
    weight = weight *2.205
    print(f"Your weight in pounds is: {weight}")
elif unit == 'p':
    weight = weight/2.205
    print(f"Your weight in kilograms is: {weight}")

else:
    print("You did not enter the unit")
