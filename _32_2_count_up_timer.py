import time


def count(start, end):
    for x in range(start, end + 1):
        print(x)
        time.sleep(0.1)
    print("DONE!")


count(10, 30)
