"""This module defines the TestLabCourse class.

Usage: 
    To execute all tests in the terminal execute the following command:
    
    $ python -m unittest tests/test_lab_course.py
"""

import unittest
from course.lab_course import LabCourse
from department.department import Department
from student.student import Student

class TestLabCourse(unittest.TestCase):
    """Tests the LabCourse class."""

    def setUp(self) -> None:
        self.name = "ISD"
        self.department = Department.COMPUTER_SCIENCE
        self.credit_hours = 90
        self.capacity = 30
        self.current_enrollment = 14
        self.lab_equipment = "Laptop"

        self.course = LabCourse(
            self.name,
            self.department,
            self.credit_hours,
            self.capacity,
            self.current_enrollment,
            self.lab_equipment
        )

    def test_init_with_lab_equipment_initialize_state(self):
        # Assert
        # Superclass private attribute
        self.assertEqual(self.name, self.course._Course__name)
        self.assertEqual(self.department, self.course._Course__department)
        self.assertEqual(self.credit_hours, self.course._Course__credit_hours)

        # Superclass protected attribute
        self.assertEqual(self.capacity, self.course._capacity)
        self.assertEqual(self.current_enrollment, self.course._current_enrollment)

        # Subclass private attribute
        self.assertEqual(self.lab_equipment, self.course._LabCourse__lab_equipment)

    def test_init_with_no_lab_equipment_initialize_state(self):
        # Arrange
        self.lab_equipment = ""

        # Act
        course = LabCourse(
            self.name,
            self.department,
            self.credit_hours,
            self.capacity,
            self.current_enrollment,
            self.lab_equipment
        )

        # Assert
        # Superclass private attribute
        self.assertEqual(self.name, course._Course__name)
        self.assertEqual(self.department, course._Course__department)
        self.assertEqual(self.credit_hours, course._Course__credit_hours)

        # Superclass protected attribute
        self.assertEqual(self.capacity, self.course._capacity)
        self.assertEqual(self.current_enrollment, course._current_enrollment)

        # Subclass private attribute
        self.assertEqual("None", course._LabCourse__lab_equipment)

    def test_str_returns_string_representation(self):
        # Act
        actual = str(self.course)

        # Assert
        expected = ("Course: ISD\n"
                    "Department: Computer Science\n"
                    "Credit Hours: 90\n"
                    "Lab Equipment: Laptop")

        self.assertEqual(expected, actual)

    def test_enroll_student_sufficient_capacity(self):
        # Arrange
        student = Student(123, "Joe Smith", Department.COMPUTER_SCIENCE)

        # Act
        actual = self.course.enroll_student(student)

        # Assert
        expected = "Joe Smith has been successfully enrolled in ISD."
        self.assertEqual(expected, actual)

    def test_enroll_student_insufficient_capacity(self):
        # Arrange
        self.current_enrollment = 15

        course = LabCourse(self.name,
                           self.department,
                           self.credit_hours,
                           self.capacity,
                           self.current_enrollment,
                           self.lab_equipment)

        student = Student(123, "Joe Smith", Department.COMPUTER_SCIENCE)

        # Act
        actual = course.enroll_student(student)

        # Assert
        expected = ("Joe Smith has NOT been enrolled in lab: ISD due "
                    "to insufficient capacity.")
        
        self.assertEqual(expected, actual)
