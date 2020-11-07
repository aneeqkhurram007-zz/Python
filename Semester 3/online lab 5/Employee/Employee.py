class Employee:
    inflationRate = 0.3
    if inflationRate > 0.5:
        annualTax = 0.05
    else:
        annualTax = 0.10
    count = 0

    def __init__(self, name="Murshad", salary=3000):
        self.name = name
        self.salary = salary
        Employee.count += 1
        self.id = Employee.count

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def computeAnnualTax(self):
        return self.salary*12*self.annualTax/100

    def computeNetSalary(self):
        self.netMonthlyIncome = self.salary - self.computeAnnualTax()
        return self.netMonthlyIncome

    @staticmethod
    def compare(emp1,  emp2):
        if emp1.salary > emp1.salary:
            print("OK")
            return emp1
        else:
            return emp2

    def display(this):
        print("\n\tEmployee " + str(this.id))
        print("Name: " + str(this.name))
        print("Salary: " + str(this.salary))
        print("Annual Tax: " + str(this.computeAnnualTax()))
        print("Net Salary: " + str(this.computeNetSalary()))

    def __str__(self):
        return "Name = "+str(self.name)+" Salary = "+str(self.salary)
