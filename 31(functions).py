# function = A block of reusable code
#           place () after the functions name to invoke it


from sys import displayhook


def happy_birthday(name, age):
    # name = "Frosty"  # replace with the birthday person's name

    print("♪ Happy birthday to you")
    print("♪ Happy birthday to you")
    print(f"♪ Happy birthday dear {name},")
    print("♪ Happy birthday to you! 🎉")
    print(f"You are {age} years old")
    print()


happy_birthday("Bro", 20)
happy_birthday("Frosty", 30)
happy_birthday("Ajaw", 40)


def display_invoice(user_name, amount, due_date):
    print(f"Hello {user_name}")
    print(f"Your bill of {amount} mora is due: {due_date}")


display_invoice("Zhongli", "10,000", "12th December")
display_invoice("Itto", "100", "12th November")


# return = statement used to end a function and send a result back to the caller


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


z = add(1, 2)
print(f"Addition: {z}")
z = sub(1, 2)
print(f"Subtraction: {z}")
z = mul(1, 2)

print(f"Multiplication: {z}")
z = div(1, 2)
print(f"Division: {z}")


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("Spongebob", "Squarepants")
print(full_name)
