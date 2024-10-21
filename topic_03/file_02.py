'''2)	Написати програму тестування функцій списків таких як: extend(), append(),
insert(id, val), remove(val), clear(), sort(), reverse(), copy()'''

fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "potato"]

# append()
fruits.append("orange ") # додає в кінець списка 
print(fruits)  

# extend()
fruits.extend(vegetables) # поєднує два списки
print(fruits)  

# insert()
fruits.insert(1, "kiwi") # за індексом вставляє в список елемент
print(fruits)  

# remove()
fruits.remove("banana") # видаляє обєкт за індексом
print(fruits)  

# sort()
fruits.sort()# сортує список
print(fruits)  

# reverse()
fruits.reverse() # в іншому порядку перевертає список
print(fruits)  

# copy()
new_fruits = fruits.copy() # робить копію 
print(new_fruits)  

# clear()
fruits.clear() # видаляє всі обєкти зі списку роблячи порожнім
print(fruits)  # []
