# list comprehensions = A concise way to create lists in python
# compact and easier to read the traditional loops
# [expression for value in iterable if condition]


doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

# doubles_list_comprehension = [expression for value in iterable if consition]

doubles_list_comprehension = [x * 2 for x in range(1, 11)]
print(doubles_list_comprehension)

triples_list_comprehension = [x * 3 for x in range(1, 11)]
print(triples_list_comprehension)

square_list_comprehension = [x * x for x in range(1, 11)]
print(square_list_comprehension)


# strings
fruits = ["apple", "orange", "banana", "coconut"]
fruit = [fruit.upper() for fruit in fruits]
print(fruit)
fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)

# conditions:

numbers = [1, -2, 3, -4, 5, -6, +8, -7]
positive_num = [num for num in numbers if num >= 0]
print(positive_num)
negative_num = [num for num in numbers if num <= 0]
print(negative_num)
even_num = [num for num in numbers if num % 2 == 0]
print(even_num)
odd_num = [num for num in numbers if num % 2 != 0]
print(odd_num)


grades = [23, 56, 89, 70, 99, 66, 20]
passing_grade = [grade for grade in grades if grade >= 33]
print(passing_grade)
