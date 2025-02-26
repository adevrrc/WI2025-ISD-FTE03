"""This module defines the StudentDecoratable class (interface)."""

__author__ = ""
__version__ = ""

from abc import ABC, abstractmethod

class StudentDecoratable(ABC):
    """This interface ..."""

    @property
    @abstractmethod
    def grade_point_average(self) -> float:
        """Returns the grade point average..."""

        pass
