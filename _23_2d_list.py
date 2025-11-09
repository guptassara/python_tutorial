fruits = ["apple", "banana", "mango", "grapes", "orange"]
vegetables = ["carrot", "spinach", "broccoli", "potato", "tomato"]
meats = ["chicken", "beef", "pork", "lamb", "fish"]

groceries = [fruits, vegetables, meats]

print(fruits)
print(vegetables)
print(meats)
print(groceries)
print(groceries[2][1])


flora_fauna = [
    ["rose", "lily", "tulip", "sunflower", "daisy"],
    ["lion", "elephant", "tiger", "giraffe", "zebra"],
    ["oak", "maple", "pine", "banyan", "neem"],
]

print(flora_fauna[2])


for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# same can be done for tuple and set too