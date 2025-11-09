# keyword argument = an argument preceded by an identifier
#                   helps with readability
#                   order of arguments doesn't matter
#                   1. positional 2. default 3. KEYWORD 4. arbitrary
#
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")


hello("Hello", "Mr.", "Spongebob", "Squarepants")
hello(
    "Hello", title="Mr.", first="Spongebob", last="Squarepants"
)  # positional arguments should come before keyword arguments
hello("Namaste", title="Ms.", last="Gupta", first="Ssara")

# examples of keyword arguments:
for x in range(1, 11):
    print(x, end=" ")

print("1", "2", "3", "4", "5", sep="-")
