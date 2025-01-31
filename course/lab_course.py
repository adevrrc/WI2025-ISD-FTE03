from course.course import Course
from department.department import Department
from student.student import Student

class LabCourse(Course):
    """TODO"""

    def __init__(self, name: str, department: Department, credit_hours: int,
                 capacity: int, current_enrollment: int, lab_equipment: str):
        """TODO"""

        # Invoke superclass constructor
        super().__init__(name, department, credit_hours, 
                         capacity, current_enrollment)
        
        lab_equipment = lab_equipment.strip()

        if len(lab_equipment) == 0:
            lab_equipment = "None"
        
        self.__lab_equipment = lab_equipment

    def enroll_student(self, student: Student) -> str:
        """Adds a student to the course if there is capacity.
        
        Args:
            student (Student): The student to be enrolled.
            
        Returns:
            The status of the student's enrollment in the course.
        """

        allowable_enrollment = int(self._capacity / 2)

        if self._current_enrollment < allowable_enrollment:
            self._current_enrollment += 1

            status = (f"{student.name} has been successfully "
                      f"enrolled in {self.name}.")
        else:
            status = (f"{student.name} has NOT been enrolled in lab: "
                      f"{self.name} due to insufficient capacity.")

        return status
