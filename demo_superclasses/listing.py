"""This module defines the Listing class."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, \
    QLabel, QLineEdit, QPushButton, QTableWidget, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Listing(QMainWindow):
    """A Python class which allows users to retrieve Client information.
    """    

    def __init__(self):
        """Initializes the Student Lookup window by adding various 
        widgets and setting properties. Widgets include: student_table.
        """

        super().__init__()

        COLUMN_HEADERS = ["Student Number", "Name", "GPA"]

        self.setWindowTitle("Student Listing")
        self.resize(600, 400) 

        # Main layout
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = QGridLayout(centralWidget)

        # Bold font for labels and headers
        bold_font = QFont()
        bold_font.setBold(True)

        self.student_table = QTableWidget()

        # Adjusting layout to make widgets centered in the middle column of a 3-column layout
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(2, 1)
        
        # Table (for Student data) span all columns
        layout.addWidget(self.student_table, 4, 0, 1, 3)  

        self.student_table.setColumnCount(3)
        self.student_table.setHorizontalHeaderLabels(COLUMN_HEADERS)                
        self.student_table.horizontalHeader().setFont(bold_font)
        self.student_table.resizeColumnsToContents()
        self.student_table.resizeRowsToContents()
  