# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.

numbers = [1, 2, 3, 4, 5]  # lists are iterable

for number in numbers:  # can used bla instead of number but name should be descriptive
    print(number, end="-")

for number in reversed(numbers):
    print(number, end=" ")

numbers_tuple = (1, 2, 3, 4, 5)
for number in numbers_tuple:
    print(number, end="-")

for number in reversed(numbers_tuple):
    print(number, end=" ")


fruits = {"apple", "orange", "banana", "mango"}  # set

for fruit in fruits:
    print(fruit, end="-")

# for fruit in reversed(fruits):
#     print(fruit, end=" ") #no reversed in sets

name = "Shivay Singh Oberoi"
for character in name:
    print(character, end=" ")
for character in reversed(name):
    print(character, end=" ")


# dictionaries:
my_dictionaries = {"A": 1, "B": 2, "C": 3}
for key in my_dictionaries:
    print(key)
for value in my_dictionaries.values():
    print(value)
for items in my_dictionaries:
    print(f"{items}: {my_dictionaries.values()}")
for key, value in my_dictionaries.items():
    print(f"{key}-{value}")
