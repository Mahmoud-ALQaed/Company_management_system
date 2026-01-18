from company_system import CompanySystem
from enums import EmployeeType

def main():
    system = CompanySystem()
    while True:
        print("""
1.Add Department 2.show_department 3.Show Departments with Employees

4.Edit Department 5.Delete Department

6.Add Worker 7.Add Manager 8.Show Employee 9.Show All Employees
              
10.Calculate Salary for Employee 11.Edit employee 12.Delete Employee

13.Assign Employee to Department 14.Remove Employee from Department

                        15.Transfer Employee

                            0.Exit
""")
        choice = input("Choose: ")

        if choice == "1":
            system.add_department()
        elif choice == "2":
            system.show_department()
        elif choice == "3":
            system.show_departments_with_employees()
        elif choice == "4":
            system.edit_department()
        elif choice == "5":
            system.delete_department()
        elif choice == "6":
            system.add_employee(EmployeeType.WORKER)
        elif choice == "7":
            system.add_employee(EmployeeType.MANAGER)
        elif choice == "8":
            system.show_employee()
        elif choice == "9":
            system.show_all_employees()
        elif choice == "10":
            system.calculate_salary_for_employee()
        elif choice == "11":
            system.edit_employee()
        elif choice == "12":
            system.delete_employee()
        elif choice == "13":
            system.assign_employee()
        elif choice == "14":
            system.remove_from_department()
        elif choice == "15":
            system.transfer_employee() 
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
