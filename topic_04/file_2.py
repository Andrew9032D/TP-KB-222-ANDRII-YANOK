'''2)	Розширити функцію ділення обробкою виняткової ситуації ділення но нуль
'''

def addition(a, b):
    return a + b 

def subtraction(a, b):
    return a - b 

def multiplication(a, b):
    return a * b

def division(a, b): # коли ділення на 0 помилка 
   if b == 0:
     return "error"
   return a / b 

while True:
    try:
        a = input("Enter first number")
     
        a = float(a)
    except ValueError: # якщо не число то помилка 
        print("Error: not a valid number.")
        continue  # Повертаємося до введення першого числа щоб не піти ділі по циклу  не з тим символом

    try:
        b = float(input("Enter second number: "))
    except ValueError:# якщо не число то помилка 
        print("Error: not a valid number.")
        continue  
   
    operation = input("What's operation [ + - * / ]: ")

    if operation == "+":
        result = addition(a, b)
        print(f"Result: {result}")

    elif operation == "-":
        result = subtraction(a, b)
        print(f"Result: {result}")

    elif operation == "*":
        result = multiplication(a, b)
        print(f"Result: {result}")

    elif operation == "/":
        result = division(a, b)
        print(f"Result: {result}")
    else:
        print("Error: invalid operation.")
