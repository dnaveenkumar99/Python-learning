class Person:
    def __init__(self):
        self.__name=""
    @property
    def dataAccess(self):
        return self.__name
    @dataAccess.setter
    def dataAccess(self,val):
        self.__name=val
p1=Person()
p1.dataAccess="Uday"
res=p1.dataAccess
print(res)