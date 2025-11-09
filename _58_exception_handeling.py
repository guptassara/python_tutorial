# exception = An event that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError)
# 1. try, 2. except, 3. finally

# 1/0
# 1+"1"
# int("Pizza")

# try:
#     #try some code
# except Exception:
#     # Handle an Exception
# finally:
#     #Do some cleanup

try:
    number = float(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")
