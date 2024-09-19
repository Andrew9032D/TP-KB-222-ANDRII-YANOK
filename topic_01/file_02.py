# 2)	Виконати тестування функцій, що працюють з рядками: strip(), capitalize(), title(), upper(), lower().
text = "???hello andrii????"
print(text.strip("?"))   # strip видаляє символи з початку рядка і кінця 


text = "hello andri"
print(text.capitalize())   # capitalize виправляє першу букву на велику всі остальні маленькі тільки перша  


text = "hello andri"
print(text.title()) # title початок слова з великої літери  не тільки діє через пробіл а й через інші символи


text = "hello andri"
print(text.upper())  # upper всі літери з великої 


text = "heSSSSSlo aEFSdri"
print(text.lower())  