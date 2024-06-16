class Employee:
    def __init__(self,dept,role,salary):
        self.dept = dept
        self.role = role
        self.salary = salary

    def showDetails(self):
        print("Dept: ",self.dept)
        print("Role: ",self.role)
        print("Salary: ",self.salary)


class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",75000)

e1 = Engineer("Elon Musk",40)
e1.showDetails()