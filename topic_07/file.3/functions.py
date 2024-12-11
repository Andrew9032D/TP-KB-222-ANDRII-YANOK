class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b


class Subtraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a - self.b


class Multiplication:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a * self.b


class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        if self.b == 0:
            return "Error: division by zero."
        return self.a / self.b