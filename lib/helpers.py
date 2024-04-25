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
    for employee in employees:
        print(employee)


def find_employee_by_name():
    employee_name = input('Input employee name: ')
    employee = Employee.find_by_name(employee_name)
    if employee:
        print(employee)
    else:
        print(f'Employee {employee_name} not found')


def find_employee_by_id():
    id_ = input('Input employee id: ')
    employee = Employee.find_by_id(id_)

    if employee:
        print(employee)
    else:
        print(f'Employee id {id_} not found')


def create_employee():
    name_ = input('Input employee name: ')
    job_title_ = input('Input job title: ')
    department_id_ = int(input('Input employee department id: '))

    try:
        employee = Employee.create(name_, job_title_, department_id_)
        print(f'Success: {employee}')
    except Exception as exc:
        print('Error creating employee', exc) 


def update_employee():
    employee_id = int(input('Input employee id: '))
    employee = Employee.find_by_id(employee_id)

    if employee:
        try:
            employee.name = input('Input new name: ')
            employee.job_title = input('Input new job title: ')
            employee.department_id = int(input('Input new department id: '))

            employee.update()
        except Exception as exc:
            print('There was an error: ', exc)
    else:
        print(f'Employee id: {employee_id} not found')


def delete_employee():
    employee_id = int(input('Input employee id: '))
    employee = Employee.find_by_id(employee_id)

    if employee:
        try:
            employee.delete()
            print(f'Employee {employee.name} successfully deleted')
        except Exception as exc:
            print('There was an error: ', exc)
    else:
        print(f'Employee {employee_id} not found')



def list_department_employees():
    dept_id = int(input('Input department id: '))
    
    try:
        department = Department.find_by_id(dept_id)
        employee_list = department.employees()
        for employee in employee_list:
            print(employee)
    except Exception as exc:
        print('There was an error: ', exc)
