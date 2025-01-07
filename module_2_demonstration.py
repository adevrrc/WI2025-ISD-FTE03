"""This module is used to demonstrate concepts from module 2."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

from student.student import Student
from department.department import Department

def main():
    """The main function of the program."""
    
    students = []
    student_number = 1000

    for i in range(10):
        name = "Student" + str(i)
        student_number += 1
        try:
            student = Student(student_number, name, Department.COMPUTER_SCIENCE)
            students.append(student)
        except ValueError as e:
            print(e)

    # 1. Create an instance of the Course class with valid inputs.
    # If an exception occurs, print the exception instance.
    # Comment out once tested.


    # 2. Define a Lecture Course with a capacity of 20 and a current enrollment of 19.
    # Use any valid values for the other parameters.
    # Print the object.


    # 3. Define a Lab Course with a capacity of 20 and a current enrollment of 8.
    # Use any valid values for the other parameters.
    # Print the object.


    # 4. Using a loop, enroll the students from the students list above
    # into the lecture course defined above.
    # Print the message returned from the enroll_student method.


    # 5. Using a loop, enroll the students from the students list above
    # into the lab course defined above.
    # Print hte message returned from the enroll_student method.

if __name__ == "__main__":
    main()
