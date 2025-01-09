"""The module defines the TestCourse class.

Example:
    $ python -m unittest tests/test_course.py
"""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

import unittest
from department.department import Department
from course.course import Course

class TestCourse(unittest.TestCase):
    """Tests for the Course class."""
     
    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        course_name = "intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        self.course = Course(course_name, department, credit_hours)

    def test_init_object_initialized_to_correct_state(self):
        # Assert
        self.assertEqual("intermediate software development", self.course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, self.course._Course__department)
        self.assertEqual(90, self.course._Course__credit_hours)

    def test_init_blank_name_raises_exception(self):
        # Arrange
        course_name = "    "
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        # Act
        with self.assertRaises(ValueError) as context:
            course = Course(course_name, department, credit_hours)

        # Assert
        expected = "Name cannot be blank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_invalid_department_raises_exception(self):
        # Arrange
        course_name ="intermediate software development"
        department = "computer science"
        credit_hours = 90

        # Act
        with self.assertRaises(ValueError) as context:
            course = Course(course_name, department, credit_hours)

        # Assert
        expected = "Department is not valid."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_invalid_credit_hours_raises_exception(self):
        # Arrange
        course_name ="intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 34.5

        with self.assertRaises(ValueError) as context:
            course = Course(course_name, department, credit_hours)

        # Assert
        expected = "Credit Hours must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_name_accessor_returns_correct_state(self):
        # Act
        actual = self.course.name

        # Assert
        expected = "intermediate software development"
        self.assertEqual(expected, actual)

    def test_department_accessor_returns_correct_state(self):
        # Act
        actual = self.course.department

        # Assert
        expected = Department.COMPUTER_SCIENCE
        self.assertEqual(expected, actual)

    def test_credit_hours_accessor_returns_correct_state(self):
        # Act
        actual = self.course.credit_hours

        # Assert
        expected = 90
        self.assertEqual(expected, actual)

    def test_str_returns_string_representation(self):
        # Act
        actual = self.course.__str__()        

        # Assert
        expected = ("Course: Intermediate Software Development\n"
                    "Department: Computer Science\n"
                    "Credit Hours: 90")
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
