'''1)	Написати функцію пошуку коренів квадратного рівняння
використовуючи функцію розрахунку дискримінанту з попередньої теми та
умовні переходи.'''

import math 

def discrim(a, b, c):
    return b**2-4*a*c

def roots(a, b, c): 
    d = discrim(a, b, c)
    
    if d > 0:
      x1 = (-b + math.sqrt(d)) / (2 * a)
      x2 = (-b - math.sqrt(d)) / (2 * a)
      print("Два корені: x1 =", x1, ", x2 =", x2)
    
    elif d == 0:
       x = -b / (2 * a)
       print("Один корінь: x =", x) 
    
    else:
     print("Коренів немає") 

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

result = roots(a, b, c)
