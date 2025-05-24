from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    if employees:
        for emp in employees:
            print(emp)
    else:
        print("No employees found.")


def find_employee_by_name():
    name = input("Enter the employee's name: ").strip()
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    try:
        emp_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(emp_id)
        if employee:
            print(employee)
        else:
            print(f"Employee {emp_id} not found")
    except ValueError:
        print("Invalid input. ID must be a number.")


def create_employee():
    name = input("Enter the employee's name: ").strip()
    job_title = input("Enter the employee's job title: ").strip()
    try:
        department_id = int(input("Enter the employee's department id: "))
        department = Department.find_by_id(department_id)
        if not department:
            print("Error: department_id must reference a department in the database")
            return
        employee = Employee.create(name=name, job_title=job_title, department_id=department_id)
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error creating employee: {e}")


def update_employee():
    try:
        emp_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(emp_id)
        if not employee:
            print(f"Employee {emp_id} not found")
            return

        name = input("Enter the employee's new name: ").strip()
        job_title = input("Enter the employee's new job title: ").strip()
        department_id = int(input("Enter the employee's new department id: "))
        department = Department.find_by_id(department_id)
        if not department:
            print("Error: department_id must reference a department in the database")
            return

        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id
        employee.update()
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error updating employee: {e}")


def delete_employee():
    try:
        emp_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(emp_id)
        if employee:
            employee.delete()
            print(f"Employee {emp_id} deleted")
        else:
            print(f"Employee {emp_id} not found")
    except ValueError:
        print("Invalid input. ID must be a number.")


def list_department_employees():
    try:
        dept_id = int(input("Enter the department's id: "))
        department = Department.find_by_id(dept_id)
        if department:
            employees = department.employees()
            if employees:
                for emp in employees:
                    print(emp)
            else:
                print(f"No employees in Department {dept_id}")
        else:
            print(f"Department {dept_id} not found")
    except ValueError:
        print("Invalid input. ID must be a number.")
