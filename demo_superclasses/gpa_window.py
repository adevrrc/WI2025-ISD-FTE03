"""This module defines the PGAWindow class."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

from PySide6.QtWidgets import QGridLayout, QLabel, QLineEdit, \
    QPushButton, QDialog, QHBoxLayout, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class GPAWindow(QDialog):
    """A Python class which allows users perform bank account 
    transactions. This class is meant to work in conjunction 
    with the BankAccount class such that deposit and withdraw 
    functionality may be used.
    """

    def __init__(self):
        """Initializes the Details window by adding various widgets and 
        setting properties. Widgets include: account_number_label, 
        balance_label, transaction_amount_label, deposit_button, 
        withdraw_button and exit_button.
        """

        # List of GRADE values
        self.GRADES = ["A+", "A", "B+", "B", "C+", "C", "D", "F"]
        self.GRADE_VALUES = [4.5, 4, 3.5, 3, 2.5, 2, 1, 0]

        # Design window.
        super().__init__()
        self.setWindowTitle("GPA Calculator")
        self.resize(200, 200)

        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignTop)  
        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(10)

        # Bold font for labels and headers
        bold_font = QFont()
        bold_font.setBold(True)

        # Account details widgets
        self.name_label = QLabel()
        self.student_number_label = QLabel()

        self.grade_header_label = QLabel("Grade")
        self.credit_hours_header_label = QLabel("Credit Hours")

        self.grade_header_label.setFont(bold_font)
        self.credit_hours_header_label.setFont(bold_font)

        self.grade_select_1 = QComboBox()
        self.grade_select_2 = QComboBox()
        self.grade_select_3 = QComboBox()

        # populate comboboxes
        self.grade_select_1.addItems(self.GRADES)
        self.grade_select_2.addItems(self.GRADES)
        self.grade_select_3.addItems(self.GRADES)

        # Credit Hours
        self.credit_edit_1 = QLineEdit()
        self.credit_edit_2 = QLineEdit()
        self.credit_edit_3 = QLineEdit()

        self.calculate_button = QPushButton("Calculate GPA")
        self.calculate_button.setEnabled(False)
        self.grade_point_average_label = QLabel()

        # Adding widgets to the overall layout.
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.student_number_label, 1, 0)
        
        layout.addWidget(self.grade_header_label, 2, 0)
        layout.addWidget(self.credit_hours_header_label, 2, 1)
   
        layout.addWidget(self.grade_select_1, 3, 0)
        layout.addWidget(self.credit_edit_1, 3, 1)

        layout.addWidget(self.grade_select_2, 4, 0)
        layout.addWidget(self.credit_edit_2, 4, 1)

        layout.addWidget(self.grade_select_3, 5, 0)
        layout.addWidget(self.credit_edit_3, 5, 1)

        layout.addWidget(self.calculate_button, 6, 0)
        layout.addWidget(self.grade_point_average_label, 6, 1)
