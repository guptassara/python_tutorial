import math
radius = float(input("Enter radius of circle: "))
circumference = 2*math.pi*radius
print(f"The circumference of the circle is: {circumference}")
area = math.pi*radius*radius
print(f"Area of the circle is: {area}")
print("Let's calculate hypotaneous of a right triangle ")
base = float(input("Enter base: "))
perpendicular = float(input("Enter perpendicular: "))
hypotaneous = math.sqrt(pow(base, 2)+pow(perpendicular,2))
print(f"The length of hypotaneous is: {hypotaneous}")