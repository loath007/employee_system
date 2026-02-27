# Employee System

"""
This module provides functionality for managing employees in an organization.
It includes features such as adding, removing, and modifying employee information,
viewing employee details, and other employee management operations.
"""

class Employee:
    """
    A class representing an employee.
    Attributes:
        name (str): The name of the employee.
        id (int): The unique identifier for the employee.
        position (str): The job position of the employee.
        salary (float): The salary of the employee.
        department (str): The department where the employee works.
    """

    def __init__(self, name, emp_id, position, salary, department):
        # Initialize an employee object with the provided attributes.
        self.name = name
        self.id = emp_id
        self.position = position
        self.salary = salary
        self.department = department

    def display_info(self):
        """
        Display the employee's information in a readable format.
        """ 
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Department: {self.department}")

    def update_salary(self, new_salary):
        """
        Update the salary of the employee.

        Parameters:
            new_salary (float): The new salary to assign to the employee.
        """
        self.salary = new_salary


class EmployeeManagement:
    """
    A class to manage a collection of employees.
    Attributes:
        employees (list): A list to store employee objects.
    """

    def __init__(self):
        # Initialize the employee management system with an empty list of employees.
        self.employees = []

    def add_employee(self, employee):
        """
        Add a new employee to the management system.

        Parameters:
            employee (Employee): An instance of the Employee class to add.
        """
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        """
        Remove an employee from the management system by ID.

        Parameters:
            emp_id (int): The ID of the employee to remove.
        """
        self.employees = [emp for emp in self.employees if emp.id != emp_id]

    def display_all_employees(self):
        """
        Display information for all employees in the system.
        """ 
        for emp in self.employees:
            emp.display_info()
            print("---")  # Separator for readability