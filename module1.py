class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(self.name + " is " + str(self.age) + " years old.")

class Student(Person):
    def __init__(self, name, age, level):
        super(Student, self).__init__(name,age)
        self.level = level

    def printInfo(self):
        print("Student ", self.name,  " is at level ", self.level)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", self.bonus)

    def toString(self):
        return "Name: "+ self.name+ ", Salary: " + self.salary+ ", Bonus: "+ self.bonus

    
A = Person("Tung",18)
A.printInfo()
B = Student("Trong", 17, "A")
B.printInfo()
C = Manager("Moth", "1000$", "200$")
print(A==A)