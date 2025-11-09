item = str(input("Enter the item you want to buy: "))
price = float(input("What is the price: "))
quantity = int(input("How many would you like?: "))

total = price*quantity

print(f"You have bought {quantity} {item}(s)")
print(f"Your total is: ₹{total}")