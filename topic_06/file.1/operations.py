
def number():
    while True:
     try:
        a = float(input("Enter first number ="))

     except ValueError: # якщо не число то помилка 
        print("Error: not a valid number.")
        continue  # Повертаємося до введення першого числа щоб не піти ділі по циклу  не з тим символом

     try:
        b = float(input("Enter second number = "))
     except ValueError:# якщо не число то помилка 
        print("Error: not a valid number.")
        continue  
     return a, b
    
def operation():
    while True:
      operation = input("What's operation [ + - * / ]: ")
      if operation in ["+", "-", "*", "/"]:
         return operation
      else:
           print("Error: invalid operation.")
     