'''2)	Маючи не відсортований список, елементами якого є словники
 з двома параметрами (ім’я та оцінка) виконати сортування списку, використовуючи 
 стандартну функцію sorted(). Другим параметром для функції sorted() має бути lambda функція, 
 що повертає ім’я або оцінку із елемента словника.'''



def sort_by_name(students):
    #Функція сортує список студентів за іменем 
    return sorted(students, key=lambda student: student["name"])

def sort_by_grade(students):
   # Функція сортує список студентів за оцінкою 
    return sorted(students, key=lambda student: student["grade"], reverse=True)


students = [
    {"name": "Anna", "grade": 90},
    {"name": "John", "grade": 85},
    {"name": "Zoe", "grade": 95},
    {"name": "Mike", "grade": 80}
]

# Сортуємо за іменем
sorted_by_name = sort_by_name(students)
print("Sorted by name:", sorted_by_name)

# Сортуємо за оцінкою
sorted_by_grade = sort_by_grade(students)
print("Sorted by grade:", sorted_by_grade)
