"""
Employee Management System
"""

import sqlite3

def create_table():
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
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO employees (name, position, salary)
                      VALUES (?, ?, ?)''', (name, position, salary))
    conn.commit()
    conn.close()

def view_employees():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(row)

def update_employee(emp_id, name, position, salary):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE employees
                      SET name = ?, position = ?, salary = ?
                      WHERE id = ?''', (name, position, salary, emp_id))
    conn.commit()
    conn.close()

def delete_employee(emp_id):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
    conn.commit()
    conn.close()

def search_employee(emp_id):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE id = ?', (emp_id,))
    record = cursor.fetchone()
    conn.close()
    return record

def main():
    create_table()

    add_employee('John Doe', 'Software Engineer', 70000)
    view_employees()

if __name__ == '__main__':
    main()