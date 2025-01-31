"""This module defines the LectureCourse class."""

__author__ = "Damien Altenburg"
__version__ = "1.1.2025"

from course.course import Course
from department.department import Department
from student.student import Student

class LectureCourse(Course):
    """Represents a course delivered with lectures."""

    def __init__(self, name: str, department: Department, credit_hours: int,
                 capacity: int, current_enrollment: int, lecture_hall: str):
        """Initializes a new instance of the LectureCourse class.

        Args:
            name (str): The name of the course.
            department (Department): The department the course is 
                delivered.
            credit_hours (int): The number of credit hours.
            capacity (int): The number of students that may enroll in 
                the course.
            current_enrollment (int): The number of students currently 
                in the course.
            lecture_hall (str): The name of the lecture hall in which 
                the course will be delivered.

        Raises:
            ValueError: Raised when the name argument value contains no 
                non-whitespace characters, the department argument value 
                is not a Department type, or the credit_hours, 
                capacity, or current_enrollment argument value is not an
                integer type.
        """
        
        super().__init__(name, department, credit_hours, capacity, current_enrollment)

        lecture_hall = lecture_hall.strip()

        if len(lecture_hall) == 0:
            raise ValueError("Lecture Hall cannot be blank.")

        self.__lecture_hall = lecture_hall

    def enroll_student(self, student: Student) -> str:
        """Enrolls the specified student in this course.
        
        Args:
            student (Student): The student being add to this course.
        
        Returns:
            str: The enrollment status.
        """

        allowable_enrollment = int(self._capacity + (self._capacity * .1))

        if self._current_enrollment < allowable_enrollment:
            self._current_enrollment += 1

            enrollment_status = (f"{student.name} has been successfully"
                                 f" enrolled in {self.name}.")
        else:
            enrollment_status = (f"{student.name} has NOT been enrolled in "
                                 f"lecture: {self.name} due to insufficient "
                                 "capacity.")

        return enrollment_status
    
    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string 
        representation of the object.

        Returns:
            str: The "informal" or nicely printable string 
                representation of the object.
        """
        
        return super().__str__() + f"\nLecture Hall: {self.__lecture_hall}"
