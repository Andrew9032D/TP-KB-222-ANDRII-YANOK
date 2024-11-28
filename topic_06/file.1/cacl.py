'''1)	Розробити механізм логування всіх дій, що виконує програма. 
Забезпечити зберігання інформації про введені данні, виконану операцію та 
результат виконання операції над даними.'''
from functions import addition, subtraction, multiplication, division
from operations import number, operation

def log_to_file(data):
    #Функція запису даних у файл логів
    with open("LOG_FILE", "a") as file:
        file.write(data + "\n")

while True:

    a, d = number()
    op = operation()
    result = None

    if op == "+":
        result = addition(a, d)
    elif op == "-":
        result = subtraction(a, d)
    elif op == "*":
        result = multiplication(a, d)
    elif op == "/":
        result = division(a, d)

    # Формуємо вид який матиме лог 
    log_entry = f"Input: {a}, {d}; Operation: {op}; Result: {result}"
    log_to_file(log_entry)  # Логування в файл

    print(f"result: {result}")
