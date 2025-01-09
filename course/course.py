"""This module defines the Course class."""

__author__ = "Damien Altenburg"
__version__ = "1.0.0"

from department.department import Department

class Course:
    """Represents a course at an educational institution."""

    def __init__(self, name: str, department: Department, credit_hours: int):
        """Initializes a new instance of the Course class.

        Args:
            name (str): The name of the course.
            department (Department): The department the course is 
                delivered.
            credit_hours (int): The number of credit hours.
        """
        self.__name = name
        self.__department = department
        self.__credit_hours = credit_hours
