# list = [] ordered and changeable. Duplicates ok
# set = {} unordered and immutable, but add/remove ok. no duplicates
# tuple = () ordered and unchangeable. duplicates ok. faster
print("LIST:")
fruits = "apple"
print(f"Fruit: {fruits}")
fruit_list = ["apple", "orange", "banana", "coconut", "coconut"]
print(f"Fruit_list: {fruit_list}")
print("NEW_list")
fruit_list.append("Pineapple")
fruit_list.insert(1, "dryfruit")
fruit_list.remove("orange")
fruit_list.reverse()
fruit_list.sort()
print(fruit_list.index("apple"))
print(fruit_list.count("coconut"))
for fruit in fruit_list:
    print(fruit)
fruit_list.clear()


# print(dir(fruit_list))
# print(help(fruit_list))
print(len(fruit_list))
print("Pineapple" in fruit_list)


print("SET")
fruit_set = {"apple", "orange", "banana", "coconut", "coconut"}
print(f"fruit set: {fruit_set}")
for fruit in fruit_set:
    print(fruit)
fruit_set.add("mangoe")
fruit_set.remove("mangoe")
fruit_set.pop()


for fruit in fruit_set:
    print(f"changed {fruit}")

print("TUPLE")
fruit_tuple = ("apple", "orange", "banana", "coconut", "apple")
print(f"fruit_tuple: {fruit_tuple}")
print(len(fruit_tuple))
print("pi" in fruit_tuple)
print(fruit_tuple.count("coconut"))

for fruit in fruit_tuple:
    print(f"new: {fruit}")
