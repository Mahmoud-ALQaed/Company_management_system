import json
from employee import Worker, Manager
from department import Department
from enums import EmployeeType


class DataStorage:
    FILE_NAME = "employees_data.json"

    @staticmethod
    def save(service):
        data = {
            "employees": [],
            "departments": []
        }

        # employees
        for emp in service.get_all_employees():
            emp_data = {
                "id": emp.id,
                "name": emp.name,
                "age": emp.age,
                "salary": emp.salary,
                "type": emp.employee_type.value,
                "bonus": getattr(emp, "bonus", None)
            }
            data["employees"].append(emp_data)

        # departments
        for dept in service.get_all_departments():
            data["departments"].append({
                "id": dept.id,
                "name": dept.name,
                "employees": list(dept.employees.keys())
            })

        with open(DataStorage.FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load(service):
        try:
            with open(DataStorage.FILE_NAME, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return

        # load employees
        for emp in data["employees"]:
            if emp["type"] == EmployeeType.WORKER.value:
                service.add_employee(
                    EmployeeType.WORKER,
                    emp["id"],
                    emp["name"],
                    emp["age"],
                    emp["salary"],
                    None
                )
            else:
                service.add_employee(
                    EmployeeType.MANAGER,
                    emp["id"],
                    emp["name"],
                    emp["age"],
                    emp["salary"],
                    emp["bonus"]
                )

        # load departments
        for dept in data["departments"]:
            service.add_department(dept["id"], dept["name"])
            department = service.get_department(dept["id"])
            for emp_id in dept["employees"]:
                emp = service.get_employee(emp_id)
                department.add_employee(emp)
