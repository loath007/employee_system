"""
Employee Management System

This module provides functionalities to manage employee records including creating, viewing, updating, searching, and deleting employee data.

Functions:
- create_table: Initializes the employee table in the database.
- add_employee: Adds a new employee record.
- view_employees: Displays all employee records.
- update_employee: Updates an existing employee record.
- delete_employee: Deletes an employee record by ID.
- search_employee: Searches for an employee by ID.
- main: Entry point of the application.
"""

import sqlite3


def create_table():
    """
    Initializes the employee table in the database.
    Creates a new SQLite database (or connects if it already exists) and creates the employee table with the necessary fields.
    """
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      position TEXT NOT NULL,
                      salary REAL NOT NULL
                      )''')
    conn.commit()
    conn.close()


def add_employee(name, position, salary):
    """
    Adds a new employee record.
    :param name: Name of the employee.
    :param position: Position of the employee.
    :param salary: Salary of the employee.
    """
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO employees (name, position, salary)
                      VALUES (?, ?, ?)''', (name, position, salary))
    conn.commit()
    conn.close()


def view_employees():
    """
    Displays all employee records.
    Fetches and prints all records in the employees table.
    """
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(row)


def update_employee(emp_id, name, position, salary):
    """
    Updates an existing employee record.
    :param emp_id: ID of the employee to update.
    :param name: New name of the employee.
    :param position: New position of the employee.
    :param salary: New salary of the employee.
    """
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE employees
                      SET name = ?, position = ?, salary = ?
                      WHERE id = ?''', (name, position, salary, emp_id))
    conn.commit()
    conn.close()


def delete_employee(emp_id):
    """
    Deletes an employee record by ID.
    :param emp_id: ID of the employee to delete.
    """
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
    conn.commit()
    conn.close()


def search_employee(emp_id):
    """
    Searches for an employee by ID.
    :param emp_id: ID of the employee to search for.
    :return: Employee record or None if not found.
    """
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE id = ?', (emp_id,))
    record = cursor.fetchone()
    conn.close()
    return record


def main():
    """
    Entry point of the application.
    Contains the main logic for managing employee records. Allows users to choose operations like view, add, update, and delete employees.
    """
    create_table()  # Ensure the table is created

    # Example operations (you can expand this to a full menu interface)
    add_employee('John Doe', 'Software Engineer', 70000)
    view_employees()


if __name__ == '__main__':
    main()