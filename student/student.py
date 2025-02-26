"""This module defines the Student class."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

import random
from department.department import Department
from patterns.singleton.singleton_student_manager import SingletonStudentManager
from patterns.decorator.student_decoratable import StudentDecoratable

class Student(StudentDecoratable):
    """Represents a student in a school."""

    def __init__(self, name: str, department: Department):
        """Initializes a new instance of the Student class.

        Args:
            name (str): The name of the student.
            department (Department): The name of the department in which
                student is enrolled.

        Raises:
            ValueError: Raised when the name contains no non-whitespace 
            characters, or the department is not a Department value.
        """

        if len(name.strip()) == 0:
            raise ValueError("Name cannot be blank.")

        if not isinstance(department, Department):
            raise ValueError("Department must be one of the predefined Departments.")

        self.__student_number = SingletonStudentManager().get_next_student_number()
        self.__name = name
        self.__department = department
        self.__grade_point_average = random.uniform(0, 4.5)

    @property
    def student_number(self) -> int:
        """Gets the student number.

        Returns:
            int: The unique id associated with the Student instance.
        """

        return self.__student_number

    @property
    def name(self) -> str:
        """Gets the student's name.

        Returns:
            str: The name of the Student instance.
        """

        return self.__name

    @property
    def department(self) -> Department:
        """Gets the name of the department in which student is enrolled.

        Returns:
            Department: A specific Department enum value associated with
                the Student instance.
        """

        return self.__department

    @property
    def grade_point_average(self) -> float:
        """Gets the student's grade point average attribute.

        Returns:
            float: The grade point average value associated with the 
                Student instance.
        """

        return self.__grade_point_average


    def __str__(self) ->str:
        """Returns a string representation of the Student instance.

        Returns:
            str: A string representation of the Student instance.
        """
        
        # Note: For departments containing more than one word
        # replace the _ with a blank.
        return (f"Student: {self.__student_number}"
                f"\nName: {self.__name}"
                f"\nDepartment: {self.__department.name.replace('_', ' ').title()}")
