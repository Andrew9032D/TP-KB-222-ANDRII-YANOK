'''4)	Використовуючи принципи ООП переписати програму Калькулятор.
 Завдання має бути виконано використовуючи модульний підхід. 

'''


from functions import Addition, Subtraction, Multiplication, Division
from operations import Number, Operation

class Calculator:
    def __init__(self):
        self.number = Number()
        self.operation = Operation()

    def run(self):
        while True:
            a, b = self.number.get_numbers()
            op = self.operation.get_operation()

            if op == "+":
                result = Addition(a, b).calculate()
            elif op == "-":
                result = Subtraction(a, b).calculate()
            elif op == "*":
                result = Multiplication(a, b).calculate()
            elif op == "/":
                result = Division(a, b).calculate()

            print(f"Result: {result}")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
