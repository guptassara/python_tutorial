op = input("Enter operator + or - or * or / ")
a= float(input("Enter 1st number "))
b= float(input("Enter 2nd number "))

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
else:
    print("You entered wrong. try again!")