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

        Raises:
            ValueError: Raised when the name argument value contains no 
                non-whitespace characters, the department argument value 
                is not a Department type, or the credit_hours argument 
                value is not an integer type.
        """

        name = name.strip()

        if len(name) == 0:
            raise ValueError("Name cannot be blank.")
        
        if not isinstance(department, Department):
            raise ValueError("Department is not valid.")

        if not isinstance(credit_hours, int):
            raise ValueError("Credit Hours must be numeric.")

        self.__name = name
        self.__department = department
        self.__credit_hours = credit_hours

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

    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string 
        representation of the object.

        Returns:
            str: The "informal" or nicely printable string 
                representation of the object.
        """

        # Isolates the enumeration value
        department = self.department.name

        # Replace underscore with spaces
        department = department.replace("_", " ")
        
        # Change the uppercase case characters to title case
        department = department.title()

        string_representation = (
            f"Course: {self.name.title()}\n"
            f"Department: {department}\n"
            f"Credit Hours: {self.__credit_hours}"
        )

        return string_representation
