
# Basic class 
class Calculation:
    def __init__(self, x, y):
        self.a = x
        self.b = y    
    def addition(self):
        total = self.a + self.b
        print("Sum: ", end = "")
        print(total)
Object_1 = Calculation(12, 12)
Object_1.addition()

# Constructor Example
class Example: 
    def __init__(self):
        print("I'm the first Contructor")
    def __init__(self):
        print("I'm the second Constructor")
    def __init__(self):
        print("I'm the third Constructor")

e = Example()

# Class Atributes
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.id}")

e = Employee("Lucas", 123)
e.details()

print(e.__doc__)
print(e.__dict__)
print(e.__module__)
print(e.__class__)