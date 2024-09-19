#3)	Написати функцію пошуку дискримінанту квадратного рівняння.

import math

def findD(a, b, c):
    
    D = b**2 - 4*a*c
    
    return D

a = int(input("Please enter start point: "))
b = int(input("Please end point: "))
c = int(input("Please enter mult: "))

result = findD(a, b, c)
print("Discriminant (D):", result)
