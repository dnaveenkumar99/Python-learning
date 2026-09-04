class Car:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name

    def setter(self,val):
        self.__name=val
    getset=property(getter,setter)
c1=Car()
c1.setter="uday"
res=c1.getter
print(res)






























