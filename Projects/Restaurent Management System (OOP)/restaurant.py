from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employees(self, employee):
        self.employees.append(employee)
        print("Employee Added!")

    def view_employees(self):
        if len(self.employees) == 0:
            print("Empty List")
        else:
            print(f"{'Employee List':<20}----------------------------------------")
            print(f"{'Name':<20}{'Phone No':<20}{'Contact Info':<20}{'Address':20}{'Age':<20}{'Designation':<20}{'Salary':<20}")
            for emp in self.employees:
                print(f"{emp.name:<20}{emp.phone:<20}{emp.email:<20}{emp.address:<20}{emp.age:<20}{emp.designation:<20}{emp.salary:<20}")