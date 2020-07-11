class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def information(self):
        return "{} {} is earning {}".format(self.first, self.last, self.pay)


emp_1 = Employee("Cemil", "Koc", 4200)
emp_2 = Employee("Mike", "Noah", 5000)

# emp_1.first = "Cemil"
# emp_1.last = "Koc"
# emp_1.pay = 4200

# emp_2.first = "Mike"
# emp_2.last = "Noah"
# emp_2.pay = 5000

print(emp_1.information())
print(emp_2.information())
