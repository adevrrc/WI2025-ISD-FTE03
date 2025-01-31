"""This module defines the Course class."""

__author__ = "Damien Altenburg"
__version__ = "1.1.2025"

from department.department import Department
from student.student import Student
from abc import ABC, abstractmethod

class Course(ABC):
    """Represents a course at an educational institution."""

    @abstractmethod
    def __init__(self, name: str, department: Department, 
                 credit_hours: int, capacity: int, 
                 current_enrollment: int):
        """Initializes a new instance of the Course class.

        Args:
            name (str): The name of the course.
            department (Department): The department the course is 
                delivered.
            credit_hours (int): The number of credit hours.
            capacity (int): The number of students that may enroll in 
                the course.
            current_enrollment (int): The number of students currently 
                in the course.

        Raises:
            ValueError: Raised when the name argument value contains no 
                non-whitespace characters, the department argument value 
                is not a Department type, or the credit_hours, 
                capacity, or current_enrollment argument value is not an
                integer type.
        """

        name = name.strip()
        
        if len(name) == 0:
            raise ValueError("Name cannot be blank.")
        
        if not isinstance(department, Department):
            raise ValueError("Department is not valid.")

        if not isinstance(credit_hours, int):
            raise ValueError("Credit Hours must be numeric.")
        
        if not isinstance(capacity, int):
            raise ValueError("Capacity must be numeric.")
        
        if not isinstance(current_enrollment, int):
            raise ValueError("Enrollment must be numeric.")

        # Private "__"
        self.__name = name
        self.__department = department
        self.__credit_hours = credit_hours

        # Protected "_"
        self._capacity = capacity
        self._current_enrollment = current_enrollment        

    @property
    def name(self) -> str:
        """Gets the name of the course.

        Returns:
            str: The name of the course.
        """

        return self.__name
    
    @property
    def department(self) -> Department:
        """Gets the department the course is delivered within.

        Returns:
            Department: The faculty department the course is managed 
                from.
        """

        return self.__department
    
    @property
    def credit_hours(self) -> int:
        """Gets the number of credit hours for this course.

        Credit hours typically correlate with the number of 
        instructional hours of a course.

        Returns:
            int: number of credit hours for this course.
        """

        return self.__credit_hours
    
    @abstractmethod
    def enroll_student(self, student: Student) -> str:
        """Enrolls the specified student in this course.
        
        Args:
            student (Student): The student being add to this course.
        
        Returns:
            str: A confirmation message indicating the enrollment 
                status.
        """
        
        pass

    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string 
        representation of the object.

        Returns:
            str: The "informal" or nicely printable string 
                representation of the object.
        """

        string_representation = ( 
            f"Course: {self.name.title()}\n"
            f"Department: {self.department.name.replace("_", " ").title()}\n" 
            f"Credit Hours: {self.credit_hours}"
        )

        return string_representation
