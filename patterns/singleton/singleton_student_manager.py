"""This module defines the SingletonStudentManager class."""

__author__ = ""
__version__ = ""

class SingletonStudentManager:
    """A class to generate the next available student number."""

    __instance = None
    __next_student_number = 2024000

    def __new__(cls):
        """Special static method that creates an instance of a class before
        it is initialized.

        Learning Note: This function is invoked before the __init__ function.

        Returns:
            SingletonStudentManager: The instance of the class.
        """

        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def get_next_student_number(self) -> int:
        """Returns the next available student number.

        Returns:
            int: The next available student number.
        """

        current_number = self.__next_student_number
        self.__next_student_number += 1
        return current_number    
