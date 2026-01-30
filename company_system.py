from storage import DataStorage
from company_service import CompanyService
from enums import EmployeeType
from utils import pause, validate_positive_int, validate_name, validate_age, validate_bonus, Check_data

class CompanySystem:
    def __init__(self):
        self.service = CompanyService()
        DataStorage.load(self.service)

    # ---------------- ADD DEPARTMENT ----------------
    def add_department(self):
        dept_id = input("Enter the department ID (a positive numerical value must be entered): ")
        if not validate_positive_int(dept_id):
            print("Invalid ID")
            pause()
            return
        
        dept_id = int(dept_id)
        if self.service.get_department(dept_id):
            print("This ID is reserved")
            pause()
            return
        
        name = input("Enter a name for the department (this field cannot be left blank): ")
        if not validate_name(name):
            print("Invalid Name")
            pause()
            return

        self.service.add_department(dept_id, name)
        print("Department added successfully")
        pause()

# ---------------- SHOW DEPARTMENT WITH EMPLOYEES ----------------
    def show_department(self):
        if not self.service.get_all_departments():
            print("No departments to display")
            pause()
            return

        dept_id = input("Enter the department ID (a positive numerical value must be entered): ")
        if not validate_positive_int(dept_id):
            print("Invalid ID")
            pause()
            return
        
        dept_id = int(dept_id)
        dept = self.service.get_department(dept_id)
        if not dept:
            print("Department not found")
            pause()
            return

        print(f"Department ID: {dept.id} | Name: {dept.name}")
        if dept.employees:
            for emp in dept.employees.values():
                print("-" * 25)
                emp.display()
        else:
            print("No employees in this department")
        pause()

    # ---------------- SHOW DEPARTMENTS WITH EMPLOYEES ----------------
    def show_departments_with_employees(self):
        departments = self.service.get_all_departments()
        if not departments:
            print("No departments to display")
            pause()
            return
        for dept in departments:
            print(f"Department ID: {dept.id} | Name: {dept.name}")
            if dept.employees:
                for emp in dept.employees.values():
                    print("-" * 25)
                    emp.display()
            else:
                print("No employees in this department")
            print("-" * 30)
            pause()

# ---------------- EDIT DEPARTMENT ----------------
    def edit_department(self):
        if not self.service.get_all_departments():
            print("No departments created")
            pause()
            return

        dept_id = input("Enter the department ID (a positive numerical value must be entered): ")
        if not validate_positive_int(dept_id):
            print("Invalid ID")
            pause()
            return
        
        dept_id = int(dept_id)
        dept = self.service.get_department(dept_id)
        if not dept:
            print("Department not found")
            pause()
            return

        name = input("Enter new department name (this field cannot be left blank): ")
        if not validate_name(name):
            print("Invalid name")
            pause()
            return
        
        self.service.edit_department(dept, name=name)
        print("Department updated successfully")
        pause()

# ---------------- DELETE DEPARTMENT ----------------
    def delete_department(self):
        departments = self.service.get_all_departments()
        if not departments:
            print("No departments created")
            pause()
            return
        
        
        if not Check_data(departments):
            print("No departments empty")
            pause()
            return

        dept_id = input("Enter the department ID (a positive numerical value must be entered): ")
        if not validate_positive_int(dept_id):
            print("Invalid ID")
            pause()
            return
        
        dept_id = int(dept_id)
        dept = self.service.get_department(dept_id)
        if not dept:
            print("Department not found")
            pause()
            return
        elif dept.employees:
            print("Department is not empty")
            pause()
            return

        self.service.delete_department(dept_id)
        print("Department deleted successfully")
        pause()

    # ---------------- ADD EMPLOYEE ----------------
    def add_employee(self, emp_type):
        emp_id = input("Enter the employee ID (a positive numerical value must be entered): ")
        if not validate_positive_int(emp_id):
            print("Invalid ID")
            pause()
            return
        
        emp_id = int(emp_id)
        if self.service.get_employee(emp_id):
            print("This ID is reserved")
            pause()
            return

        name = input("Enter the employee's name (this field cannot be left blank): ")
        if not validate_name(name):
            print("Invalid NAME")
            pause()
            return

        age = input("Enter the employee's age (entry of age under 18 is not allowed): ")
        if not validate_age(age):
            print("Invalid Age")
            pause()
            return
        age = int(age)

        salary = input("Enter the employee's salary (must be a positive numerical value greater than 0): ")
        if not validate_positive_int(salary):
            print("Invalid Salary")
            pause()
            return
        salary = int(salary)

        bonus = None
        if emp_type == EmployeeType.MANAGER:
            bonus = input("Enter the employee bonus (a positive numerical value must be entered): ")
            if not validate_bonus(bonus):
                print("Invalid Bonus")
                pause()
                return
            bonus = int(bonus)

        self.service.add_employee(emp_type, emp_id, name, age, salary, bonus)
        print("The employee has been added successfully")
        pause()

    # ---------------- SHOW EMPLOYEE ----------------
    def show_employee(self):
        if not self.service.get_all_employees():
            print("No employees available")
            pause()
            return

        emp_id = input("Enter the employee ID (a positive numerical value must be entered): ")
        if not validate_positive_int(emp_id):
            print("Invalid ID")
            pause()
            return
        
        emp_id = int(emp_id)
        emp = self.service.get_employee(emp_id)
        if not emp:
            print("Employee unavailable")
            pause()
            return
        emp.display()
        pause()

    # ---------------- SHOW ALL EMPLOYEES ----------------
    def show_all_employees(self):
        employees = self.service.get_all_employees()
        if not employees:
            print("No employees available")
            pause()
            return
        
        for emp in employees:
            emp.display()
            print("-" * 30)
            pause()

    # ---------------- EDIT EMPLOYEE ----------------
    def edit_employee(self):
        if not self.service.get_all_employees():
            print("No employees available")
            pause()
            return

        emp_id = input("Enter the employee ID (a positive numerical value must be entered): ")
        if not validate_positive_int(emp_id):
            print("Invalid ID")
            pause()
            return
        
        emp_id = int(emp_id)
        emp = self.service.get_employee(emp_id)
        if not emp:
            print("Employee unavailable")
            pause()
            return

        name = input("Enter a new name or (press Enter to skip): ")
        if not validate_name(name):
            print("Skipped")
            pause()
        else:
            self.service.edit_employee(emp, name=name)
            print("Name updated")
            pause()

        age = input("Enter new Age or (press Enter to skip): ")
        if not validate_age(age):
            print("Skipped")
            pause()
        else:
            age = int(age)
            self.service.edit_employee(emp, age=age)
            print("Age updated")
            pause()

        salary = input("Enter new salary or (press Enter to skip): ")
        if not validate_positive_int(salary):
            print("Skipped")
            pause()
        else:
            salary = int(salary)
            self.service.edit_employee(emp, salary=salary)
            print("Salary updated")
            pause()

        if emp.employee_type == EmployeeType.MANAGER:
            bonus = input("Enter new bonus or (press Enter to skip): ")
            if not validate_bonus(bonus):
                print("Skipped")
                pause()
                return
            bonus = int(bonus)
            self.service.edit_employee(emp, bonus=bonus)
            print("Bonus updated")
            pause()

    # ---------------- DELETE EMPLOYEE ----------------
    def delete_employee(self):
        if not self.service.get_all_employees():
            print("No employees available")
            pause()
            return

        emp_id = input("Enter the employee ID (a positive numerical value must be entered): ")
        if not validate_positive_int(emp_id):
            print("Invalid ID")
            pause()
            return
        
        emp_id = int(emp_id)
        if not self.service.get_employee(emp_id):
            print("Employee unavailable")
            pause()
            return
        
        self.service.delete_employee(emp_id)
        print("Employee deleted successfully")
        pause()

    # ---------------- calculate salary for employee -------------
    def calculate_salary_for_employee(self):
        if not self.service.get_all_employees():
            print("No employees available")
            pause()
            return

        emp_id = input("Enter the employee ID (a positive numerical value must be entered):  ")
        if not validate_positive_int(emp_id):
            print("Invalid ID")
            pause()
            return
        
        emp_id = int(emp_id)
        emp = self.service.get_employee(emp_id)
        if not emp:
            print("Employee unavailable")
            pause()
            return
        print(f"Final Salary for ID [{emp.id}]  NAME [{emp.name}] IS: {emp.calculate_salary()}")
        pause()

    # ---------------- ASSIGN ----------------
    def assign_employee(self):
        if not self.service.get_all_employees():
            print("No employees available")
            pause()
            return
        
        departments = self.service.get_all_departments()
        if not departments:
            print("No departments available")
            pause()
            return

        emp_id = input("Enter the employee ID (a positive numerical value must be entered): ")
        if not validate_positive_int(emp_id):
            print("Invalid ID")
            pause()
            return
        
        emp_id = int(emp_id)
        emp = self.service.get_employee(emp_id)
        if not emp:
            print("Employee unavailable")
            pause()
            return
        
        for dept in departments:
            if dept.employees:
                if emp_id in dept.employees:
                    print("This employee is already within the department")
                    pause()
                    return

        dept_id = input("Enter the department ID (a positive numerical value must be entered): ")
        if not validate_positive_int(dept_id):
            print("Invalid ID")
            pause()
            return
        
        dept_id = int(dept_id)
        dept = self.service.get_department(dept_id)
        if not dept:
            print("Department not found")
            pause()
            return
        
        self.service.assign_employee_to_department(emp, dept)
        print("The employee was successfully added to the department")
        pause()

# ----------------  REMOVE  ----------------
    def remove_from_department(self):
        departments = self.service.get_all_departments()
        if not departments:
            print("No departments available")
            pause()
            return

        if not Check_data(departments, True):
            print("No department contains any data")
            pause()
            return
            
        dept_id = input("Enter the department ID (a positive numerical value must be entered): ")
        if not validate_positive_int(dept_id):
            print("Invalid ID")
            pause()
            return
        
        dept_id = int(dept_id)
        dept = self.service.get_department(dept_id)
        if not dept:
            print("Department not found")
            pause()
            return
        elif not dept.employees:
            print("no employees in this department")
            pause()
            return
            
        emp_id = input("Enter the employee ID (a positive numerical value must be entered): ")
        if not validate_positive_int(emp_id):
            print("Invalid ID")
            pause()
            return
        
        emp_id = int(emp_id)
        emp = self.service.get_employee(emp_id)
        if not emp:
            print("Employee unavailable")
            pause()
            return
        elif emp_id not in dept.employees:
            print("The employee could not be found in the department. Please verify the ID of both the employee and the department")
            pause()
            return
        
        self.service.remove_employee_from_department(dept, emp_id)
        print("The employee was successfully removed from the department")
        pause()

# ---------------- TRANSFER ----------------
    def transfer_employee(self):
        departments = self.service.get_all_departments()
        if not departments:
            print("No departments available")
            pause()
            return

        if not Check_data(departments, True):
            print("No department contains any data")
            pause()
            return
        
        if len(departments) < 2:
            print("Number of departments less than 2")
            pause()
            return

        source_id = input("Enter source department ID (a positive numerical value must be entered): ")
        if not validate_positive_int(source_id):
            print("Invalid ID")
            pause()
            return
        
        source_id = int(source_id)
        dept_1 = self.service.get_department(source_id)
        if not dept_1:
            print("Department not found")
            pause()
            return
        elif not dept_1.employees:
            print("no employees in this department")
            pause()
            return

        emp_id = input("Enter the employee ID (a positive numerical value must be entered): ")
        if not validate_positive_int(emp_id):
            print("Invalid ID")
            pause()
            return
        
        emp_id = int(emp_id)
        emp = self.service.get_employee(emp_id)
        if not emp:
            print("Employee unavailable")
            pause()
            return
        elif emp_id not in dept_1.employees:
            print("The employee could not be found in the department. Please verify the ID of both the employee and the department")
            pause()
            return

        target_id = input("Enter target department ID (a positive numerical value must be entered): ")
        if not validate_positive_int(target_id):
            print("Invalid ID")
            pause()
            return
        
        target_id = int(target_id)
        dept_2 = self.service.get_department(target_id)
        if not dept_2:
            print("Department not found")
            pause()
            return
        elif emp_id in dept_2.employees:
            print("Transfer failed; no different section was selected")
            pause()
            return
        
        self.service.transfer_employee(dept_1, emp_id, dept_2, emp)
        print("Transfer completed successfully")
        pause()
