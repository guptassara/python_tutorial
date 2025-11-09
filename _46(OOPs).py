# object = a "bundle" of related attributes (variables) and methods (functions)
# eg.
# phone:
#     def dial_phone
#     def pick_phone
# cup:
#     def fill_cup(    )
#     def empty_cup()
# bok:
#     def read_book()
#     def open_book()

# class = (blueprint) used to design the structure and layout of an object
#
# methods = actions that objects can perform


from _46_car import Car


car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "Blue", True)
car3 = Car("Charger", 2015, "Black", True)

print(car1.model)  # . is the attribute access operator
print(car1.year)
print(car1.colour)
print(car1.for_sale)

print(car1.model)
print(car2.year)
print(car2.colour)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.colour)
print(car3.for_sale)

car1.drive()
car2.drive()
car3.drive()
car1.stop()
car2.stop()
car3.stop()
car1.describe()
car2.describe()
car3.describe()
