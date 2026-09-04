class Heart:
    def __init__(self):
        self.status="Dead"
    def getheart(self):
        print("Getting heart")
class Person:
    def __init__(self,name):
        self.pname=name
        self.h=Heart()
        self.c=""
    def hascar(self,p):
        self.c=p
class Car:
    def __init__(self,name):
        self.cname=name
    def getcar(self):
        print("Car is getting")
p1=Person("Naveen")
c1=Car("Tata")
p1.hascar(c1)
print(p1.pname)
print(p1.h.status)
p1.h.getheart()
p1.c.getcar()
del p1
print(c1.cname)
print(p1.h.status)

