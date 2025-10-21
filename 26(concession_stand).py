menu = {
    "pizza": 249,
    "burger": 149,
    "pasta": 199,
    "sandwich": 129,
    "fries": 99,
    "momos": 119,
    "wrap": 159,
    "coffee": 89,
    "chocolate shake": 139,
    "ice cream": 179,
}

cart = []  # empty list
total = 0

print("🌸✨ Welcome to Frosty Café ✨🌸")
print("=" * 40)
for key, value in menu.items():
    print(f"{key:20}: ₹{value:.2f}")
print("=" * 40)
print("💖 Thank you for visiting! 💖")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("=" * 40)
print("🌸🌸Your billing summary🌸🌸")
for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")

print()

print(f"Total amount is: ₹{total:.2f}")
