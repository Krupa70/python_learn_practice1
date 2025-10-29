from itertools import count


class Employee:
    __slots__ = ('emp_name', 'emp_id', 'salary')  # restrict dynamic attributes
    
    type = "Temporary" # class level constructor

    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id
    
    add_salary = lambda self, amount: setattr(self, 'salary', amount)

    def update_id(self, new_id):
        self.emp_id = new_id  # instance method to update emp_id
        
    def display_info(self):
        salary = getattr(self, "salary", "N/A")
        print("Employee details")
        print("-----------------")
        print(f"  Name  : {self.emp_name}")
        print(f"  ID    : {self.emp_id}")
        print(f"  Salary: {salary}")  # instance method

# Run the code 
employee = Employee("John", "E101")

Employee.type = "Permanent"
print(f"Employee Type: {Employee.type}")

employee.add_salary(5000)
employee.display_info()

setattr(employee, 'emp_id', 'E102')

update_name_fn = lambda self, new_name: setattr(self, 'emp_name', new_name)
setattr(Employee, 'update_name', update_name_fn)

