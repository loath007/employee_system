import sqlite3

def create_table():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT
)
""")
    conn.commit()
    conn.close()

def add_employee():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    name = input("Enter employee name: ")
    while True:
        try:
            age = int(input("Enter employee age:"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid age.")

    department = input("Enter employee department: ")

    cursor.execute(
        "INSERT INTO employees(name,age,department) VALUES(?,?,?)",
        (name,age,department)
    )

    conn.commit()
    conn.close()
    print("Employee added successfully.\n")


def view_employees():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\n---Employees List---")

    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]} Age: {row[2]}, Department: {row[3]}")
    
    conn.close()
    print()

def update_employee():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    while True:
        try:
            emp_id = int(input("Enter employee id to update:"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid employee id.")

    new_department = input("Enter new department: ")

    cursor.execute(
        "UPDATE employees SET department = ? WHERE id = ?",
        (new_department,emp_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        print("No employee found with the given ID.")
    else:
        print("Employee updated successfully.")

    conn.close()


def delete_employee():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    while True:
        try:
            emp_id = int(input("Enter employee id to delete:"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid employee id.")

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (emp_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        print("No employee found with the given ID.")
    else:
        print("Employee deleted successfully.")

    conn.close()

def search_employee():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    name = input("Enter name to search: ")

    cursor.execute(
        "SELECT * FROM employees WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    rows = cursor.fetchall()

    if rows:
        print("\n---Search Results---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")
    else:
        print("No employee found with the given name.")

    conn.close()
    print()


def main():
    create_table()

    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_employee() 
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            search_employee()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__": 
    main()

