foods = []
prices = []
total = 0

while True:
    food = str(input("Enter a food to buy (q to quit): "))
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: ₹"))
        foods.append(food)
        prices.append(price)

print("----😍Your cart😍-----")

for food in foods:
    print(f"You prdered {food}")

for price in prices:
    total = total + price

print(f"Your total is ₹{total}")
