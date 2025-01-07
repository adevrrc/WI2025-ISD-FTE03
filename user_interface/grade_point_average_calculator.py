"""This defines the GradePointAverageCalculator class."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, Signal

class GradePointAverageCalculator():
    """Represents a window that allows for GradePointAverage to be 
    calculated.
    
    Inherited from GPAWindow which provides the gui design.
    """
    
    def __init__(self, student_number: str, name: str):
        """Initializes the window widgets and displays received data.
        
        Args:
            student_number (str): The student number of the student 
                being displayed.
            name (str): The name of the student being displayed.
        """

        self.GRADE_LOOKUP = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, 
                            "C+": 2.5, "C": 2, "D": 1, "F": 0}

    def __enable_button(self):
        """Validates the input fields and if valid, enables the 
        Calculate button.
        """
        pass
       
    def __on_calculate_clicked(self):
        """Calculates the grade point average based on the data 
        provided.

        Emits a signal with the student number and calculated gpa when 
        complete.
        """
        #Formula: 
        # ((grade1 * cr_hours1) + (grade2 * cr_hours2) + etc) / sum(cr_hours#)
