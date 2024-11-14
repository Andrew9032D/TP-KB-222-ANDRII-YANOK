'''3)	Використання модулів для програми калькулятор. Функції додавання, віднімання,
 множення та ділення перенести в файл functions.py. 
 Функції запиту на введення даних для операцій та самих операцій перемістити в файл operations.py.
   Програму калькулятор реалізувати в файлі calc.py, до якого підключають файл functions.py та operations.py.'''
from functions import addition, subtraction, multiplication, division
from operations import number, operation

while True:
    a,d = number()
    op = operation()

    if op == "+":
        result = addition(a,d)
    elif op == "-":
        result = subtraction(a,d)
    elif op == "*":
        result = multiplication(a,d)
    elif op == "/":
        result = division(a,d)

    print (f"result: {result}")