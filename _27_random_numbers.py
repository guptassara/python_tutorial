import random

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


print("prints random integer")
print(random.randint(low, high))
print("prints random floating point number")
print(random.random())
option = random.choice(options)
print(option)
random.shuffle(cards)
print(cards)
