'''4)	Маючи відсортований список, написати функцію пошуку
позиції для вставки нового елементу в список.'''

def find_insert_position(sorted_list, new_element): # пошук потрібної позиції
    position = 0
    for element in sorted_list: # перебір всіх елементів 
        if new_element < element:
            break
        position += 1
    return position

def insert_and_print(sorted_list, new_element):
    # Знаходимо позицію для вставки
    position = find_insert_position(sorted_list, new_element)
    
    # Вставляємо новий елемент на знайдену позицію
    sorted_list.insert(position, new_element)
    
    # Виводимо оновлений список
    print("Updated list:", sorted_list)


sorted_list = [1, 3, 4, 7, 9, 10]
new_element = 11
insert_and_print(sorted_list, new_element)
