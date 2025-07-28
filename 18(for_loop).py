for i in range(1, 11):  # last number is exclusive so its 1 to 10
    print(i)

print("Reversed")
for count in reversed(range(1, 11, 2)):
    print(count)
print("Happy new year!!!!!!!")

print("String")
credit_card = "1234-4567-7890"
for j in credit_card:
    print(j)

print("Break")
for i in range(1, 30):
    if i == 7:
        break
    print(i)

print("Continue")
for i in range(1, 22):
    if i == 5:
        continue
    print(i)
