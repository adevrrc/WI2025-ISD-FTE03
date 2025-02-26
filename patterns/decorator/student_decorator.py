"""This module defines the StudentDecorator class."""

__author__ = ""
__version__ = ""

from patterns.decorator.student_decoratable import StudentDecoratable

class StudentDecorator(StudentDecoratable):
    """Represents the base decorator class for wrapping other Student 
    type objects.
    """
    
    def __init__(self, student: StudentDecoratable):
        """Initializes a new instance of the StudentDecorator class.

        Args:
            student (StudentDecoratable): The student to be decorated.
        """

        self.__student = student

    @property
    def grade_point_average(self) -> float:
        """Returns the student's grade point average.

        Returns:
            float: The student's grade point average.
        """
        
        return self.__student.grade_point_average
