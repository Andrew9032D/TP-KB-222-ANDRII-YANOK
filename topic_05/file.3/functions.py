'''3)	Використання модулів для програми калькулятор. Функції додавання, віднімання,
 множення та ділення перенести в файл functions.py. 
 Функції запиту на введення даних для операцій та самих операцій перемістити в файл operations.py.
   Програму калькулятор реалізувати в файлі calc.py, до якого підключають файл functions.py та operations.py.'''

def addition(a, b):
    return a + b 

def subtraction(a, b):
    return a - b 

def multiplication(a, b):
    return a * b

def division(a, b): # коли ділення на 0 помилка 
   if b == 0:
     return "Error: division by zero."
   return a / b 