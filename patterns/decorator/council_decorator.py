"""This module defines the CouncilDecorator class."""

__author__ = ""
__version__ = ""

from patterns.decorator.student_decorator import StudentDecorator

class CouncilDecorator(StudentDecorator):
    """Represents a student who participates in student council while 
    studying.
    """

    @property
    def grade_point_average(self) -> float:
        """Returns the student's grade point average.

        The student receives an increases to their GPA dependant on their
        current GPA.

        Returns:
            float: The student's grade point average.
        """
        
        grade_point_average = super().grade_point_average

        increases = {
            4.13: .35,
            3.67: .19,
            2.4: .04
        }

        increase = 0

        for average in increases:
            if grade_point_average >= average:
                increase = increases[average]
                break

        return grade_point_average + increase