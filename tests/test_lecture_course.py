"""This module defines the TestLectureCourse class.

Usage: 
    To execute all tests in the terminal execute the following command:
    
    $ python -m unittest tests/test_lecture_course.py
"""

import unittest
from course.lecture_course import LectureCourse
from department.department import Department
from student.student import Student

class TestLectureCourse(unittest.TestCase):
    """Tests the LectureCourse class."""

    def setUp(self) -> None:
        self.name = "ISD"
        self.department = Department.COMPUTER_SCIENCE
        self.credit_hours = 90
        self.capacity = 30
        self.current_enrollment = 28
        self.lecture_hall = "P107"

        self.course = LectureCourse(self.name,
                                    self.department,
                                    self.credit_hours,
                                    self.capacity,
                                    self.current_enrollment,
                                    self.lecture_hall)

    def test_init_initialize_state(self):
        # Assert
        # Superclass private attribute
        self.assertEqual(self.name, self.course._Course__name)
        self.assertEqual(self.department, self.course._Course__department)
        self.assertEqual(self.credit_hours, self.course._Course__credit_hours)

        # Superclass protected attribute
        self.assertEqual(self.capacity, self.course._capacity)
        self.assertEqual(self.current_enrollment, self.course._current_enrollment)

        # Subclass private attribute
        self.assertEqual(self.lecture_hall, self.course._LectureCourse__lecture_hall)

    def test_init_lecture_hall_is_blank_raises_exception(self):
        # Arrange
        self.lecture_hall = ""

        # Act
        with self.assertRaises(ValueError) as context:
            course = LectureCourse(
                self.name,
                self.department,
                self.credit_hours,
                self.capacity,
                self.current_enrollment,
                self.lecture_hall
            )

        # Assert
        self.assertEqual("Lecture Hall cannot be blank.", str(context.exception))

    def test_str_returns_string_representation(self):
        # Act
        actual = str(self.course)

        # Assert
        expected = ("Course: ISD\n"
                    "Department: Computer Science\n"
                    "Credit Hours: 90\n"
                    "Lecture Hall: P107")

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
        self.current_enrollment = 31

        course = LectureCourse(self.name,
                               self.department,
                               self.credit_hours,
                               self.capacity,
                               self.current_enrollment,
                               self.lecture_hall)

        student = Student(123, "Joe Smith", Department.COMPUTER_SCIENCE)

        # Act
        actual = course.enroll_student(student)

        # Assert
        expected = ("Joe Smith has NOT been enrolled in lecture: ISD "
                   "due to insufficient capacity.")
        
        self.assertEqual(expected, actual)
