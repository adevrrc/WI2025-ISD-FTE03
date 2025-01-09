"""This module is used to demonstrate concepts from module 1."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

from course.course import Course
from department.department import Department

def main():
    """The main function of the program."""
    
    # 1. Create an instance of the Course class with valid inputs.
    #    Print the instance.
    #    If an exception occurs, print the exception instance.
    try:
        course = Course("Intermediate Software Development", 
                        Department.COMPUTER_SCIENCE, 
                        90)

        print(course)
    except ValueError as error:
        print(error)
    
    # 2. Create an instance of the Course class with invalid inputs.
    # Print the instance.
    # If an exception occurs, print the exception instance.
    try:
        course = Course("   ", Department.COMPUTER_SCIENCE, 90)

        #course = Course("", Department.COMPUTER_SCIENCE, 90)

        #course = Course("Intermediate Software Development", 45.6, 90)

        #course = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE, "90")

        print(course)
    except ValueError as error:
        print(error)
    
if __name__ == "__main__":
    main()
