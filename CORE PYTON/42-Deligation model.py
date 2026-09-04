# class Radio:
#     def turnOn(self,n):
#         if n==1:
#             print("Radio is ON")
#         else:
#             print("Radio is OFF")
# class Car:
#     def __init__(self,min,max):
#         self.Cmin=min
#         self.Cmax=max
#         self.r=Radio()
# c1=Car(30,120)
# print(c1.Cmin)
# print(c1.Cmax)
# c1.r.turnOn(1)
# c1.r.turnOn(0)

#compostiton
class OS:
    def __init__(self):
        self.status=True
        print("OS is installing")
    def getos(self):
        print("OS is installig")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=OS()
        print("Mobile is ready")
        print("with OS installed")
M1=Mobile("Nokia")
print(M1.mname)
print(M1.o.status)
M1.o.getos()
del M1
print(M1.o.status)

#aggregation
# class Charger:
#     def __init__(self,name):
#         self.cname=name
#     def getcharger(self):
#         print("get mobile charger")
# class Mobile:
#     def __init__(self,name):
#         self.mname=name
#         self.c=""
#     def hasMobile(self,p):
#         self.c=p
# m1=Mobile("Nokia")
# c1=Charger("Cpin")
# m1.hasMobile(c1)
# print(m1.mname)
# print(m1.c.cname)
# m1.c.getcharger()
# del m1
# print(c1.cname)
# c1.getcharger