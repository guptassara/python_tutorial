price1 = 18786786767.34159
price2 = -8823
price3 = 292

print("2 decimal places")
print(f"Price1 is ₹{price1:.2f}")
print(f"Price2 is ₹{price2:.2f}")
print(f"Price3 is ₹{price3:.2f}")

print("10 spaces")
print(f"Price1 is ₹{price1:10}")
print(f"Price2 is ₹{price2:10}")
print(f"Price3 is ₹{price3:10}")

print("0 padded")
print(f"Price1 is ₹{price1:010}")
print(f"Price2 is ₹{price2:010}")
print(f"Price3 is ₹{price3:010}")

print("Left justify the value")
print(f"Price1 is ₹{price1:<10}")
print(f"Price2 is ₹{price2:<10}")
print(f"Price3 is ₹{price3:<10}")

print("Right justify the value")
print(f"Price1 is ₹{price1:>10}")
print(f"Price2 is ₹{price2:>10}")
print(f"Price3 is ₹{price3:>10}")

print("Center justify the value")
print(f"Price1 is ₹{price1:^10}")
print(f"Price2 is ₹{price2:^10}")
print(f"Price3 is ₹{price3:^10}")

print("Pawsitive values value")
print(f"Price1 is ₹{price1:+10}")
print(f"Price2 is ₹{price2:+10}")
print(f"Price3 is ₹{price3:+10}")

print("Pawsitive values value")
print(f"Price1 is ₹{price1: 10}")
print(f"Price2 is ₹{price2: 10}")
print(f"Price3 is ₹{price3: 10}")

print("Negative values values value")
print(f"Price1 is ₹{price1:-}")
print(f"Price2 is ₹{price2:-}")
print(f"Price3 is ₹{price3:-10}")

print("comma")
print(f"Price1 is ₹{price1:,}")
print(f"Price2 is ₹{price2:,}")
print(f"Price3 is ₹{price3:,}")

print("something else")
print(f"Price1 is ₹{price1:+,.2f}")
print(f"Price2 is ₹{price2:+,.2f}")
print(f"Price3 is ₹{price3:+,.2f}")
