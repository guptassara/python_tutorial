principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle: "))
    if principle < 0:
        print("Principle can not be less than or equal to zero")
    else:
        break
print(principle)

while True:
    rate = float(input("Enter the rate: "))
    if rate < 0:
        print("rate can not be less than or equal to zero")
    else:
        break
print(rate)

while True:
    time = float(input("Enter the time: "))
    if time < 0:
        print("time can not be less than or equal to zero")
    else:
        break
print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year(s): ₹{total: .2f}")
