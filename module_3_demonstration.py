"""This module is used to demonstrate concepts from module 3."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

from student.student import Student
from department.department import Department
from course import *

def main():
    """The main function of the program."""
    
    students = []

    students.append(Student(20240000, "John Brunelle", Department.MEDICINE))
    students.append(Student(20240001, "Elizabeth Sinclair", Department.COMPUTER_SCIENCE))
    students.append(Student(20240002, "Angela Brock", Department.EDUCATION))
    students.append(Student(20240002, "Robert Flammand", Department.MEDICINE))
    students.append(Student(20240003, "Arthur Armstrong", Department.COMPUTER_SCIENCE))
    students.append(Student(20240002, "Chris Mullin", Department.EDUCATION))
    students.append(Student(20240003, "Jackie Blanchard", Department.MEDICINE))
    students.append(Student(20240004, "George Shanahan", Department.COMPUTER_SCIENCE))
    students.append(Student(20240005, "Linda Eck", Department.EDUCATION))
    students.append(Student(20240006, "Judy Gardener", Department.MEDICINE))
    students.append(Student(20240007, "Donna Smith", Department.COMPUTER_SCIENCE))
    students.append(Student(20240008, "Eric Best", Department.EDUCATION))

    for student in students:
        print(f"\n{str(student)}")

        ### DECORATOR ###

if __name__ == "__main__":
    main()
