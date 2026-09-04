class Student:
    def __init__(self):
        self.name = "Uday"
        self.age  = 21
        self.usn  = 420
    def study(self):
        print("Uday is not studying")
s1=Student()
print(s1.name)
print(s1.age)
print(s1.usn)
s1.study()