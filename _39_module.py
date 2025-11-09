# module = a file containing code you want to include in your program
# use 'import' to inlude (built-in or your on)
# useful to break up a large program reusabe seperate files
#


# print(help("modules"))
# print(help("math"))


import math

print(math.pi)
import math as m

print(m.pi)
from math import pi

print(pi)

from math import e

print(e)
a, b, c, d, e = 1, 2, 3, 4, 5
print(e**a)
print(e**b)
print(e**c)
print(e**d)
print(e**e)


import _39_module_example

result = _39_module_example.pi
result = _39_module_example.square(2)
result = _39_module_example.cube(5)
result = _39_module_example.circumference(25)
result = _39_module_example.area(45)
