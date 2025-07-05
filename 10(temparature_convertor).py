temp = float(input("Enter the temparature: "))
unit = input("Enter the unit c/f")
if unit == 'c':
    tempf = (temp*9/5)+32
    print(f"Temparature in fahrenheit is: {tempf}")
elif unit =='f':
    tempc = (temp-32)*5/9
    print(f"Temparature in celsius is: {tempc}")
else:
    print("You did not enter the unit!")