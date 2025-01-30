from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def __init__(self, employee_id: int):
        self.__employee_id = employee_id

    @property
    def employee_id(self) -> int:
        return self.__employee_id
    
    @abstractmethod
    def calculate_pay(self) -> float:
        """Returns the amount the employee is paid.
        
        Returns:
            float: The amount the employee is paid.
        """
        
        pass
    
    def __str__(self) -> str:
        return "Employee"
    
class HourlyEmployee(Employee):
    def __init__(self, employee_id: int, hours_worked: int, rate_of_pay: float):
        super().__init__(employee_id)

        self.__hours_worked = hours_worked
        self.__rate_of_pay = rate_of_pay

    def calculate_pay(self) -> float:
        """Returns the amount the employee is paid.
        
        Returns:
            float: The amount the employee is paid.
        """
        
        return self.__hours_worked * self.__rate_of_pay

    def __str__(self) -> str:
        return "HourlyEmployee"
    
def main():
    #employee = Employee(123)
    #print(employee.employee_id)

    #print(type(employee))

    #print(employee)

    employee = HourlyEmployee(234, 40, 10)
    print(employee.employee_id)

    print(type(employee))

    print(isinstance(employee, Employee))
    print(isinstance(employee, HourlyEmployee))

    print(employee.__str__())

    print(employee.calculate_pay())

if __name__ == "__main__":
    main()
