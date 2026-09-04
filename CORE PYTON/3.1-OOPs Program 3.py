class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def talk(self):
        print("My rollno is:",self.rollno)
        print("My name is:",self.name)
s1=Student(100,"Bunny")
s1.talk()

