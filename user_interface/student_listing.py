"""This module defines the StudentListing class."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt, Slot
from student.student import Student
from department.department import Department

class StudentListing():
    """Represents a window which displays student data.

    Inherited from Listing which provides the gui design.
    """

    def __init__(self):
        """Initialize a new instance of the StudentListing class."""

        self.students = []
        self.students.append(Student("Janine Wharton", Department.COMPUTER_SCIENCE))
        self.students.append(Student("Freddie Jeffries", Department.MEDICINE))
        self.students.append(Student("Paul Thompson", Department.COMPUTER_SCIENCE))
        self.students.append(Student("Suzanne Marchand", Department.EDUCATION))
        
    def __on_select_student(self, row: int, column: int):
        """Obtain values from a clicked row.

        Connected to the cellClicked event of a QTable and therefore 
        has row/column arguments.

        Args:
            row (int): Row that has been clicked on.
            column(int): Column that has been clicked on.
        """
        pass

    def __update_grade_point_average(self, student_number: str, 
                                     grade_point_average: float):
        """Updates the GPA value based on updates made in another 
        window. The other window sends a signal upon updating, and this 
        slot receives the signal.

        Args:
            student_number (str): The impacted student number.
            gpa (float): The updated gpa value.
        """
        pass
