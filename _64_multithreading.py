# multithreading = Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like readinf files or fetching data from API
# threading.Thread(target = my_function).

import threading
import time


# Running on the same thread
def walk_dog(first, last):
    time.sleep(8)
    print(f"You finished walking the dog {first} {last}")


def take_out_trash():
    time.sleep(2)
    print("You took out the trash")


def get_mail():
    time.sleep(4)
    print("You got the mail")


walk_dog("Chinchila", "chiki")
take_out_trash()
get_mail()

# all at the same time...concurrently, multithreading
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()
chore2 = threading.Thread(target=take_out_trash)
chore2.start()
chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")
