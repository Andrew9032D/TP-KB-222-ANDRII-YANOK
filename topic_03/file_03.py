'''3)	Написати програму тестування функцій словників таких як:
 update(), del(), clear(), keys(), values(), items()'''
 

# словник
person = {"name": "Alice", "age": 25, "city": "New York"}

# Оновлення словника
person.update({"age": 26, "job": "Engineer"})
print(person)  

# Видалення пари ключ-значення
del person["city"]
print(person)  

# Перегляд всіх ключів
print(person.keys())  

# Перегляд всіх значень
print(person.values())  

# Перегляд всіх пар ключ-значення
print(person.items())  

# Очистка словника
person.clear()
print(person) 