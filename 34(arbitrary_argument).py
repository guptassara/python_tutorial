# *args = allows you to pass multiple non-key arguments     tuple
# **kwargs = allows you to pass multiple keyword-arguments  dictionary
#           *unpacking operator
#           1. positional 2. default 3. KEYWORD 4. ARBITRARY
def add(a, b):
    return a + b


print(add(1, 2))


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 90, 8, 76, 89.07))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


display_name("Mr.", "Kyryll", "Chudomirovich", "Flins")
print(display_name)


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(
    house="100", street="AB Road", city="Indore", state="Madhya Pradesh", zip=44021
)
