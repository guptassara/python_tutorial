# variable scope = where a variable is visible and accessible
# scope resolution= (LEGB) local -> Enclosed -> Global -> Built-in

x = 20  # Global


def func1():
    a = 1  # local scope
    print(a)
    # print(b)
    print(x)


def func2():
    b = 2
    # print(a)
    print(b)
    x = 30
    print(x)


def func3():
    # b = 3   #1st local then we see enclosed
    func2()  # enclosed
    # print(b)


func1()
func2()
func3()

# Built-in
from math import e


def func4():
    print(e)


func4()
e = 3  # (LEGB order)
func4()
