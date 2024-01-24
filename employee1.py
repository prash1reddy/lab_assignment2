class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id} {self.name} {self.age} {self.salary}"


class EmployeeSorting:
    @staticmethod
    def main():
        employees = [
            Employee("161E90", "Ramu", 35, 59000),
            Employee("171E22", "Tejas", 30, 82100),
            Employee("171G55", "Abhi", 25, 100000),
            Employee("152K46", "Jaya", 32, 85000)
        ]

        print("Choose sorting parameter:")
        print("1. Age\n2. Name\n3. Salary")

        sorting_parameter = input("Enter the number corresponding to the sorting parameter: ")
        sorting_parameter = int(sorting_parameter)

        employees.sort(key=lambda emp: (
            emp.age if sorting_parameter == 1 else
            emp.name if sorting_parameter == 2 else
            emp.salary
        ))

        print("\nSorted Employee Table:")
        for employee in employees:
            print(employee)


if __name__ == "__main__":
    EmployeeSorting.main()
