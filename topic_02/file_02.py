'''2)	Написати програму калькулятор використовуючи if else конструкцію.
Кожна операція має бути виконана в окремій функції.'''

def addition(a, b):
    return a + b 

def subtrction(a, b):
    return a - b 

def multiplication(a, b):
    return a * b

def division(a, b): # коли ділення на 0 помилка 
   if b == 0:
       return "error"
   return a / b 

a = int(input("a = "))
b = int(input("b = "))

operation = input ("What's operation [ + - * /]")

if operation == "+":
    result = addition(a, b)
    print (result)

elif operation == "-":
    result = subtrction(a, b)
    print (result)

elif operation == "*":
 result = multiplication(a, b)
 print (result)

elif operation == "/":
    result = division(a, b)
    print (result)

else:
    print ("eror")

