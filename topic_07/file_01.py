'''2)	Ознайомитись з існуючими за замовченням
 методами класу по типу __init__(self) __str__(self)__ 
та надати приклади використання.'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Product(name='{self.name}', price={self.price} UAH)"

# Створення об'єкта класу
product = Product("Laptop", 15000)
print(product)  
