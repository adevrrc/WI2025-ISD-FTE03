"""This module defines the VolunteerDecorator class."""

__author__ = ""
__version__ = ""

from patterns.decorator.student_decorator import StudentDecorator

class VolunteerDecorator(StudentDecorator):
    """Represents a student who completes volunteer work related to 
    their studies.
    """
    
    @property
    def grade_point_average(self) -> float:
        """Returns the student's grade point average.

        The student receives a .25 increase to their GPA.

        Returns:
            float: The student's grade point average.
        """
        
        return super().grade_point_average + .25
