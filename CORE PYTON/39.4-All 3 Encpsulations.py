#Noraml Encapsulation
# class Car:
#     def __init__(self):
#         self.__brand=""
#     def setter(self,val):
#         self.__brand=val
#     def getter(self):
#         return self.__brand
# c1=Car()
# c1.setter("TATA")
# res=c1.getter()
# print(res)

#Encapsulation using property()
# class Car:
#     def __init__(self):
#         self.__brand=""
#     def getter(self):
#         return self.__brand
#     def setter(self,val):
#         self.__brand=val
#     getset=property(getter,setter)
# c1=Car()
# c1.getset="TATA"
# res=c1.getset
# print(res)

#@property decorator in encapsulation
class Car:
    def __init__(self):
        self.__brand=""
    @property
    def disp(self):
        return self.__brand
    @disp.setter
    def disp(self,val):
        self.__brand=val
c1=Car()
c1.disp="TATA"
res=c1.disp
print(res)