class Number:
    def get_numbers(self):
        while True:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                return a, b
            except ValueError:
                print("Error: not a valid number. Please enter valid numbers.")

class Operation:
    def get_operation(self):
        while True:
            operation = input("Choose operation [ + - * / ]: ")
            if operation in ["+", "-", "*", "/"]:
                return operation
            else:
                print("Error: invalid operation. Please choose from [ + - * / ].")