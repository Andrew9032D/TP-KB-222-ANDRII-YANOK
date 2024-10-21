'''1)	Написати програму калькулятор з постійними запитами на введення нових даних та операцій.
За основу взяти програму калькулятор з попередньої теми. 
Реалізувати механізм завершення програми після отримання відповідної команди.'''
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

while True:
 
 a = input("enter first number (or 'exit' to quit): ")
 if a == "exit":
    break
 b = input("enter second number: ")
  

 operation = input ("What's operation [ + - * /]")

 a = float(a)
 b = float(b)

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