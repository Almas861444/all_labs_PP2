#1
import math

degree = float(input("degree: "))
rad = math.radians(degree)
print("radian:", rad)

#2
import math
a = float(input("Height: "))
b = float(input("Base, first value: "))
c = float(input("Base, second value: "))
trapezoid = (b + c) * 0.5 * a
print("Expected Output:", trapezoid)

#3
import math
n = int(input("Input number of sides: "))
a = float(input("Input the lenght of a side: "))
r = a / (2 * math.tan(math.pi/n))
area = 0.5 * n * a * r
print("The are of the polygon is:", area)

#4
import math
a = int(input("Lenght of base: "))
b = int(input("Height of parallelogram: "))
print("Expected Output:", a * b)