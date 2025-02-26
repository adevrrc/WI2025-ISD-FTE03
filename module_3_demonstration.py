"""This module is used to demonstrate concepts from module 3."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

from student.student import Student
from department.department import Department
from course import *
from patterns.singleton.singleton_student_manager import SingletonStudentManager
from patterns.decorator.volunteer_decorator import VolunteerDecorator
from patterns.decorator.council_decorator import CouncilDecorator

def main():
    """The main function of the program."""

    # obj = SingletonStudentManager()
    # print(type(obj))
    # print(id(obj))

    # obj2 = SingletonStudentManager()
    # print(type(obj2))
    # print(id(obj2))
    
    students = []

    # students.append(Student(20240000, "John Brunelle", Department.MEDICINE))
    # students.append(Student(20240001, "Elizabeth Sinclair", Department.COMPUTER_SCIENCE))
    # students.append(Student(20240002, "Angela Brock", Department.EDUCATION))
    # students.append(Student(20240002, "Robert Flammand", Department.MEDICINE))
    # students.append(Student(20240003, "Arthur Armstrong", Department.COMPUTER_SCIENCE))
    # students.append(Student(20240002, "Chris Mullin", Department.EDUCATION))
    # students.append(Student(20240003, "Jackie Blanchard", Department.MEDICINE))
    # students.append(Student(20240004, "George Shanahan", Department.COMPUTER_SCIENCE))
    # students.append(Student(20240005, "Linda Eck", Department.EDUCATION))
    # students.append(Student(20240006, "Judy Gardener", Department.MEDICINE))
    # students.append(Student(20240007, "Donna Smith", Department.COMPUTER_SCIENCE))
    # students.append(Student(20240008, "Eric Best", Department.EDUCATION))

    students.append(Student("John Brunelle", Department.MEDICINE))
    students.append(Student("Elizabeth Sinclair", Department.COMPUTER_SCIENCE))
    students.append(Student("Angela Brock", Department.EDUCATION))
    students.append(Student("Robert Flammand", Department.MEDICINE))
    students.append(Student("Arthur Armstrong", Department.COMPUTER_SCIENCE))
    students.append(Student("Chris Mullin", Department.EDUCATION))
    students.append(Student("Jackie Blanchard", Department.MEDICINE))
    students.append(Student("George Shanahan", Department.COMPUTER_SCIENCE))
    students.append(Student("Linda Eck", Department.EDUCATION))
    students.append(Student("Judy Gardener", Department.MEDICINE))
    students.append(Student("Donna Smith", Department.COMPUTER_SCIENCE))
    students.append(Student("Eric Best", Department.EDUCATION))

    for student in students:
        print(f"\n{str(student)}")

        ### DECORATOR ###
    
    print("\n", "*" * 40, "\n", sep="")

    student = students[0]
    print(student)
    print(f"Initial GPA: {student.grade_point_average}")

    student = CouncilDecorator(student)
    print(f"On Student Council GPA: {student.grade_point_average}")

    student = VolunteerDecorator(student)
    print(f"On Student Council & Volunteer GPA: {student.grade_point_average}")

if __name__ == "__main__":
    main()
