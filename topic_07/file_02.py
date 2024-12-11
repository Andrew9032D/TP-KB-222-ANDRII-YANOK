'''3)	Розробити клас Student атрибутами якого э два параметра name та age. 
Створити список елементами якого є об'єкти класу Student. Написати цикл який виводить на екран елементи списку у відсортованому порядку.
 Для сортування використати стандартну функцію sorted. Функція sorted має використовувати lambda функцію для визначення ключа сортування.'''

class Student:
    def __init__(self, name, age):
        if not name:
            raise ValueError("ERROR: Empty name")
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

# Створення списку студентів
def create_students():
    students = []
    
    # Додаємо кілька студентів
    students.append(Student("Іван", 22))
    students.append(Student("Олена", 20))
    students.append(Student("Максим", 23))
    students.append(Student("Анна", 21))
    
    return students

# Головна функція для виведення відсортованого списку студентів
def main():
    students = create_students()

    # Сортуємо список студентів за ім'ям
    sorted_students = sorted(students, key=lambda student: student.name)
    
    # Виводимо відсортовані елементи
    for student in sorted_students:
        print(student)


main()
