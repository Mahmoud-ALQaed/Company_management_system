from employee import Worker, Manager
from department import Department
from enums import EmployeeType

class CompanyService:
    def __init__(self):
        self._departments = {}
        self._employees = {}

# ---------------- DEPARTMENT ----------------
    def add_department(self, dept_id, name):
        self._departments[dept_id] = Department(dept_id, name)

    def get_department(self, dept_id):
        return self._departments.get(dept_id)
        
    def get_all_departments(self):
        return list(self._departments.values())

    def edit_department(self, dept, *, name=None):
        if name is not None:
            dept.name = name

    def delete_department(self, dept_id):
        del self._departments[dept_id]

    # ---------------- EMPLOYEE ----------------
    def add_employee(self, emp_type, emp_id, name, age, salary, bonus):
        if emp_type == EmployeeType.WORKER:
            self._employees[emp_id] = Worker(emp_id, name, age, salary)
        else:
            self._employees[emp_id] = Manager(emp_id, name, age, salary, bonus)

    def get_employee(self, emp_id):
        return self._employees.get(emp_id)

    def get_all_employees(self):
        return list(self._employees.values())

    def edit_employee(self, emp, *, name=None, age=None, salary=None, bonus=None):
        
        if name is not None:
            emp.name = name
        
        if age is not None:
            emp.age = age
        
        if salary is not None:
            emp.salary = salary
        
        if bonus is not None: 
            emp.bonus = bonus

    def delete_employee(self, emp_id):
        for dept in self._departments.values():
            if dept.employees:
                if emp_id in dept.employees:
                    dept.remove_employee(emp_id)

        del self._employees[emp_id]

    # ---------------- Operations ----------------
    def assign_employee_to_department(self, emp, dept):
        dept.add_employee(emp)

    def remove_employee_from_department(self, dept, emp_id):
        dept.remove_employee(emp_id)

    def transfer_employee(self, dept_1, emp_id, dept_2, emp):
        dept_1.remove_employee(emp_id)
        dept_2.add_employee(emp)
