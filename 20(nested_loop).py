for i in range(3):
    for j in range(1, 10):
        print(j, end=" ")
    print()


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for x in range(rows):
    for y in range(columns):
        print("🟥", end="")
    print()
