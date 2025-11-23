# Class Inheritance Chain 


class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

class Manager(Person):
    def __init__(self, name, age, ):
        super().__init__(name, age)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def total_salary(self):
        return sum(emp.salary for emp in self.employees)


# Example usage:
e1 = Employee("Alice", 30, 50000)
e2 = Employee("Bob", 25, 60000)

m1 = Manager("Charlie", 40)
m1.add_employee(e1)
m1.add_employee(e2)

print(f"Manager: {m1.name}, Total Salary of Employees: {m1.total_salary()}")  # Output: Manager: Charlie, Total Salary of Employees: 110000