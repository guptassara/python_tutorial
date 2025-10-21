# dictionary: a colletion of {key:value} pairs
# ordered and changeable. No duplicates
capitals = {
    "India": "New Delhi",
    "Russia": "Moscow",
    "China": "Beijing",
    "Japan": "Tokyo",
}
print(dict(capitals))
# print(help(capitals))
print(capitals.get("India"))
print(capitals.get("USA"))

if capitals.get("Russia"):
    print("Exists")
else:
    print("Does not exist")

capitals.update({"Germany": "Berlin"})
print(dict(capitals))
capitals.update({"Germany": "idk"})
print(dict(capitals))
capitals.pop("China")
print(dict(capitals))
capitals.popitem()  # removes the last item
print(dict(capitals))
# capitals.clear()
# print(dict(capitals))

# to get all keys:
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(f"Keys are: {key}")

# to get all values:
for value in capitals.values():
    print(f"Values are: {value}")


items = capitals.items()  # resembles 2d tuples
for key, value in capitals.items():
    print(f"{key}: {value}")
