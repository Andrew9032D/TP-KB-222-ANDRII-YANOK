import pytest
from student import Student
from student_list import StudentList

def test_add_student():
    student_list = StudentList()
    student = Student("Alice", "0631234567", "Math", "Kyiv")
    student_list.add_student(student)
    assert len(student_list.students) == 1

def test_remove_student():
    student_list = StudentList()
    student = Student("Alice", "0631234567", "Math", "Kyiv")
    student_list.add_student(student)
    student_list.remove_student("Alice")
    assert len(student_list.students) == 0

def test_update_student():
    student_list = StudentList()
    student = Student("Alice", "0631234567", "Math", "Kyiv")
    student_list.add_student(student)
    student_list.update_student("Alice", phone="0637654321")
    assert student_list.students[0].phone == "0637654321"
